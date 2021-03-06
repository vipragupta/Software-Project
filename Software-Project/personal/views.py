from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_list_or_404
from django.contrib import auth
from django.template.context_processors import csrf
#from django.core.context_processors import csrf
#from django.views.decorators import csrf

#Import all the forms from form.py
from .forms import ProjectModelForm
from .forms import StudentForm
from .models import ProjectModel
from .models import Student
from .forms import *
from .models import DEPARTMENT as DEP
from django.db.models import Q
import copy
import pandas as pd

#-------------Create your views here-------------------------
def home(request):
	return render(request, "personal/home.html")

#-------------Student views-----------------------------------
def viewprojects(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_student.html')
	all_projs = list( ProjectModel.objects.all() )
	context = {}
	details1 = []
 
	for i in all_projs:
		add = []
		add.append(i.Id)
		add.append(i.Appr_Title)
		add.append(i.Appr_Details)
		add.append(i.PF_Department)
		add.append(i.Appr_Special_Requirements)  
		add.append(i.PF_First_Name + "\n" + i.PF_Last_Name)  
		add.append(i.PF_Contact_Number)  
		add.append(i.PF_Email)
		details1.append(add)

	dep_grp = {}
 
	for dep in DEP:
		all_projs = list( ProjectModel.objects.filter(PF_Department = dep[0]) )
		project = []
		for proj in all_projs:
			add = []
			add.append(proj.Id)
			add.append(proj.Appr_Title)
			add.append(proj.Appr_Details)
			add.append(proj.PF_Department)
			add.append(proj.Appr_Special_Requirements)  
			add.append(proj.PF_First_Name + "\n" + i.PF_Last_Name)  
			add.append(proj.PF_Contact_Number)  
			add.append(proj.PF_Email)
			project.append(add)
		if len(project)> 0:   
			dep_grp[dep[1]] = copy.deepcopy(project)

	faculty_grp = {}
	facultyNames = ProjectModel.objects.order_by().values('PF_First_Name', 'PF_Last_Name').distinct()

	for faculty in facultyNames:
		values = faculty.values()     
		name = values[0] + " ".decode("utf-8") + values[1]
		all_projs = list( ProjectModel.objects.filter(PF_First_Name = values[0], PF_Last_Name = values[1]) )
		project = []
		for proj in all_projs:
			
			add = []
			add.append(proj.Id)
			add.append(proj.Appr_Title)
			add.append(proj.Appr_Details)
			add.append(proj.PF_Department)
			add.append(proj.Appr_Special_Requirements)  
			add.append(proj.PF_First_Name + "\n" + i.PF_Last_Name)  
			add.append(proj.PF_Contact_Number)  
			add.append(proj.PF_Email)
			project.append(add)
			   
		if len(project)> 0:   
			faculty_grp[ name ] = copy.deepcopy(project)
		
	context["details1"] = details1
	context["dep_grp"] = dep_grp
	context["faculty_grp"] = faculty_grp
	return render(request, 'personal/viewprojects.html', context)

def applyprojects(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_student.html')
	studentForm = StudentForm(request.POST or None)
	projectRequirementDic = getProjectRequirementList()
	context = {
		"studentForm": studentForm,
		"projectRequirementDic":projectRequirementDic
	}
	if request.method == "POST":
		if studentForm.is_valid():

			instance = studentForm.save(commit=False)
			instance.save()

			return render(request, 'personal/studenthome.html',context)

	return render(request, 'personal/applyprojects.html',context)	

def updateRequirements(request, sid):
	print sid
	projectList = list(Student.objects.filter(Student_Id = sid))
	RequirementList = []
	
	for projectId in projectList:
		tempReqList = list(ProjectModel.objects.filter(Id = str(projectId)))
		RequirementList.append(tempReqList.Requirement1)
		RequirementList.append(tempReqList.Requirement2)
		RequirementList.append(tempReqList.Requirement3) 
	
	labelName = ["P1_Req1","P1_Req2","P1_Req3","P2_Req1","P2_Req2","P2_Req3","P3_Req1","P3_Req2","P3_Req3","P4_Req1","P4_Req2","P4_Req3","P5_Req1","P5_Req2","P5_Req3"]
	
	instance = get_object_or_404(StudentForm, Student_Id=sid)
	form = UpdateReqForm(request.POST or None, instance=instance)
	
	for i in range(len(RequirementList)):
		form.setlabel(labelname[i], RequirementList[i])
	
	context = {"updateReqForm", form}
	#proj_req = list(ProjectModel.objects.filter(Id = id) )
	if form.is_valid():
		form.save()
		return render(request, 'personal/studenthome.html', context)

def getProjectRequirementList():
	projectRequirementDic = {}
	projects = list( ProjectModel.objects.all())

	for project in projects:
		projectRequirementList = [project.Requirement1, project.Requirement2, project.Requirement3]
		projectRequirementDic[project.Id] = projectRequirementList
		
	return projectRequirementDic

def facultyhome(request):
    if not request.user.is_authenticated():
		return render_to_response('personal/login_faculty.html')
    return render(request, 'personal/facultyhome.html')

def studenthome(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_student.html')
	return render(request, 'personal/studenthome.html')

#----------------Faculty views----------------------------------------
def projects(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_faculty.html')
	username = request.user.username
	all_projs = list( ProjectModel.objects.filter(Username = username) )
	context = {}
	details1 = []
 
	for i in all_projs:
		add = []
		add.append(i.Id)
		add.append(i.Appr_Title)
		add.append(i.Appr_Details)
		add.append(i.PF_Department)
		add.append(i.Appr_Special_Requirements)  
		add.append(i.PF_First_Name + "\n" + i.PF_Last_Name)  
		add.append(i.PF_Contact_Number)  
		add.append(i.PF_Email)
		details1.append(add)
	context["details1"] = details1
	return render(request, 'personal/projects.html', context)

def rawmatrix(request):
	if not request.user.is_authenticated():
		return render_to_response('personal/login_faculty.html')
	print "In raw Matrix"
	username = request.user.username
	projectList = []
	projects = list(ProjectModel.objects.filter(Username = username))

	for projectEntry in projects:
		d = {}
		projectId = projectEntry.Id
		projectName = projectEntry.Appr_Title
		temp = {"projectId":projectId}
		d.update(temp)
		temp = {"projectName":projectName}
		d.update(temp)
		#print "projectId:" + str(projectId)+":			Name: ", projectName
		#studentInfo = list(Student.objects.filter(First_Preference = str(projectId)))#.filter(Two_Preference = str(projectId)).filter(Three_Preference = str(projectId)).filter(Four_Preference = str(projectId)).filter(Five_Preference = str(projectId)))
		studentInfo = list(Student.objects.filter(Q(First_Preference = str(projectId)) | Q(Two_Preference = str(projectId)) | Q(Three_Preference = str(projectId)) | Q(Four_Preference = str(projectId)) | Q(Five_Preference = str(projectId))))
		#print "studentInfo: ", studentInfo
		studentList = []
		
		for student in studentInfo:
			studentInfoDic = {}
			name = student.First_Name + " " + student.Last_Name
			temp={"studentName":name}
			studentInfoDic.update(temp)
			temp={"studentGpa":student.GPA}
			studentInfoDic.update(temp)
			temp={"major":student.Primary_Major}
			studentInfoDic.update(temp)
			preferance = " "

			if (student.First_Preference == str(projectId)):
				preferance = "First"
			elif (student.Two_Preference == str(projectId)):
				preferance = "Second"
			elif (student.Three_Preference == str(projectId)):
				preferance = "Third"
			elif (student.Four_Preference == str(projectId)):
				preferance = "Fourth"
			elif (student.Five_Preference == str(projectId)):
				preferance = "Fifth"
			#print "Converted preferance: ", preferance
			
			temp={"preferance":preferance}
			studentInfoDic.update(temp)
			temp={"req1":"First req"}#student.req1}
			studentInfoDic.update(temp)
			temp={"req2":"Second req"}#student.req2}
			studentInfoDic.update(temp)
			temp={"req3":"Third req"}#student.req3}
			studentInfoDic.update(temp)
			temp={"skill1":student.Skills_1}
			studentInfoDic.update(temp)
			temp={"skill2":student.Skills_2}
			studentInfoDic.update(temp)
			temp={"skill3":student.Skills_3}
			studentInfoDic.update(temp)
			studentList.append(studentInfoDic)
			#print studentInfoDic
		temp1={"Students":studentList}
		d.update(temp1)
		projectList.append(d)
	context = {}
	details1 = []	
 
	'''
	for projectEntry in projects:
		projectId = projectEntry.Id
		getStudentList(projectId)
	'''
	#Temporary()
      
	context["projectData"] = projectList
	matrixtoxcel()
	return render(request, 'personal/raw_data_matrix.html', context)
 
#This is temporary database modification, not part of logic
def Temporary():
    all_projs = list( ProjectModel.objects.all( ))
    for proj in all_projs:
        proj.Requirement1 = "C++"
        proj.Requirement2 = "Java"
        proj.Requirement3 = "Python"
        proj.save()
    return

def editEligibleStudents(request):
	context = {}

	if request.method == 'POST':
		if request.is_ajax():
			if 'id' in request.POST:
				projectId = request.POST['id']
				print projectId
				students = getStudentList(projectId)
				arr = []
				for student in students:
					name = student.First_Name + " ".decode("utf-8") + student.Last_Name
					arr.append([student.Student_Id, name, student.GPA, student.Primary_Major] )                
                
				context["students"] = arr
				return HttpResponse(projectId)    
    
				#print context
	return render(request, 'personal/editEligibleStudents.html', context)


#Use this function to get students that are eligible for a project.
def getStudentList(projectId):
    project = list(ProjectModel.objects.filter(Id = projectId))[0]
    newlist = []
    studentInfo = list(Student.objects.filter(Q(First_Preference = str(projectId)) |
        Q(Two_Preference = str(projectId)) | 
        Q(Three_Preference = str(projectId)) | 
        Q(Four_Preference = str(projectId)) | 
        Q(Five_Preference = str(projectId))))
        
    preference = list()
    
    req = []
    print project.Requirement1
    print project.Requirement2
    print project.Requirement3
    if project.Requirement1 != "none":
        req.append(1)
    
    if project.Requirement1 != "none":
        req.append(2)
        
    if project.Requirement1 != "none":
        req.append(3)
    
    #print projectId
    for i in studentInfo:
        #print i.First_Name, i.Last_Name, "\n"
        #print i.Project_selected_for, type(i.Project_selected_for)
        
        if i.Project_selected_for != 0:
            #print i.First_Name, i.Last_Name, "already selected"
            print i.Student_Id, "Project_selected_for"
            continue
        
        if float(i.GPA) < float(project.Min_GPA):
            print i.Student_Id, "GPA"
            continue
        
        if int(i.Availability) == 0:
            print i.Student_Id, "Availability"
            continue
        
        if int(i.Got_DLA_Before) == 1:
            print i.Student_Id, "DLA_Before"
            continue
        
        if int(i.Enrollment) == 0:
            print i.Student_Id, "Enrollment"
            continue
        
        if  i.Degree_Level == "MS":
            print i.Student_Id, "MS"
            continue
        elif i.Level == "FSE":
            print i.Level, "DegreeLevel"
            continue
        
        if i.First_Preference == project.Id:
		if (i.P1_Req1 == "0" and project.Requirement1 != "none") or (i.P1_Req2 == "0" and project.Requirement2 != "none") or (i.P1_Req3 == "0" and project.Requirement3 != "none"):
			continue 
        elif i.Two_Preference == project.Id:
		if (i.P2_Req1 == "0" and project.Requirement1 != "none") or (i.P2_Req2 == "0" and project.Requirement2 != "none") or (i.P2_Req3 == "0" and project.Requirement3 != "none"):
    			continue
        elif i.Three_Preference == project.Id:
		if (i.P3_Req1 == "0" and project.Requirement1 != "none") or (i.P3_Req2 == "0" and project.Requirement2 != "none") or (i.P3_Req3 == "0" and project.Requirement3 != "none"):
    			continue
        elif i.Four_Preference == project.Id:
		if (i.P4_Req1 == "0" and project.Requirement1 != "none") or (i.P4_Req2 == "0" and project.Requirement2 != "none") or (i.P4_Req3 == "0" and project.Requirement3 != "none"):
    			continue
        elif i.Five_Preference == project.Id:
		if (i.P5_Req1 == "0" and project.Requirement1 != "none") or (i.P5_Req2 == "0" and project.Requirement2 != "none") or (i.P5_Req3 == "0" and project.Requirement3 != "none"):
    			continue
        
        newlist.append(i)
        print i.Student_Id, i.Degree_Level, i.Availability, i.Got_DLA_Before, i.Level
        
    print projectId, newlist
    return newlist
    
def project(request, pid):
    	print pid
    	return render(request, 'personal/projects.html', {})

def addprojects(request):
    
	if not request.user.is_authenticated():
		return render_to_response('personal/logout.html')

	projectModelForm = ProjectModelForm(request.POST or None)
	
	context = {
		"projectModelForm": projectModelForm,
		#"projectRequirementDic":projectRequirementDic
	}
	if request.method == "POST":
		
		if projectModelForm.is_valid():
			#print projectModelForm.cleaned_data
			instance = projectModelForm.save(commit=False)
			if request.user.is_authenticated():
				username = request.user.username
   			instance.Username = username
			instance.save()
			return render(request, 'personal/facultyhome.html',context)

	return render(request, 'personal/addprojects.html',context)	



#Login Authentication related views ---- login_faculty() to logout()
def login_faculty(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('personal/login_faculty.html', c)

def login_student(request):
    c = {}
    c.update(csrf(request))
    '''
    myuserForm = MyuserForm(request.POST or None)
    print csrf(request)
    #print k
    context = {
		"myuserForm": myuserForm
    }

    if request.method == "POST":
        
        print k
        #This is only for database		
        if myuserForm.is_valid():
            instance = myuserForm.save(commit=False)
            #instance.User = csrf(request)
            instance.save()
    '''
    return render(request, 'personal/login_student.html',c)
 
def auth_view_faculty(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, 'personal/facultyhome.html')	
    else:
        return HttpResponseRedirect('invalid')

def auth_view_student(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, 'personal/studenthome.html')	
    else:
        return HttpResponseRedirect('invalid')

def loggedin(request):
    return render_to_response('personal/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('personal/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('personal/logout.html')
    

 ########################Matching Algorithm#######################################





def matchedMatrix(request):
	context = {}

	if request.method == 'POST':
		if request.is_ajax():
			print "request.POST:   ", request.POST
			projectsData = createProjectDataDictionary(list(ProjectModel.objects.all()))
 			studentsData = createStudentDataDictionary(list(Student.objects.all()))
			print "\n"
			for item in request.POST:
				print "\n\n^^", str(item), str(request.POST[item])
				projectId = str(item)
				studentId = str(request.POST[item])
				
				if projectId != "csrfmiddlewaretoken":

					projectId = projectId.replace("id[", "")
					projectId = projectId.replace("]", "")

					print "###", projectId, studentId
					project = projectsData[projectId]
					oldAssignedStudent = project.Student_Selected
					
					print "$$$", projectId, studentId, oldAssignedStudent

					
					if studentId != "None":
						student = studentsData[studentId]
						student.Project_selected_for = projectId
						project.IS_Facutly_Selected = "1"
						project.Student_Selected = studentId
					else:
						student = studentsData[oldAssignedStudent]
						student.Project_selected_for = ""
						project.Student_Selected = ""
						project.IS_Facutly_Selected = "0"

					project.save()
					student.save()

			return HttpResponse(projectId)


	matchedMatrixAlgorithm()
	details1 = []
	context["matched"] = createContextForMatchedMatrix()
	return render(request, 'personal/matchedMatrix.html', context)


def matchedMatrixAlgorithm():
	print "******************Starting**************************"
	projectsData = createProjectDataDictionary(list(ProjectModel.objects.all()))
 	studentsData = createStudentDataDictionary(list(Student.objects.all()))
 	projectToStudentMap = {}					#value as -1 means that no student applied for that projectremoveStudentsWhoDontSatisfyBareMinimumReq
 	removeStudentsWhoDontSatisfyBareMinimumReq(studentsData)
 	removeProjectIdList = removeSelectedStudents(projectsData, studentsData)
 	studentListForEachProjectId = getStudentToProjectMaps(projectsData, studentsData, removeProjectIdList)

 	matchedFlag = 1
 	while (matchedFlag):
 		print "\n\nLooping..."
 		print "***studentListForEachProjectId: ", studentListForEachProjectId
	 	discardProjectsWithZeroStudents(studentListForEachProjectId, projectToStudentMap)
	 	matchProjectsWithOneStudents(studentListForEachProjectId, studentsData, projectToStudentMap, projectsData)
	 	matchedFlag = removeAssignedStudents(studentListForEachProjectId, projectToStudentMap)

 	matchProjectsWithMoreThanOneStudents(studentListForEachProjectId, studentsData, projectToStudentMap)
 	updateDataInDb(projectToStudentMap)
 	print "******************Ending**************************"


def createContextForMatchedMatrix():
	print "\n\n\n"
	projectsData = createProjectDataDictionary(list(ProjectModel.objects.all()))
 	studentsData = createStudentDataDictionary(list(Student.objects.all()))
 	studentListForEachProjectId = getNewStudentToProjectMaps(projectsData, studentsData)
 	#print "studentListForEachProjectId:   ", studentListForEachProjectId
 	context = []

 	for projectId in projectsData:
 		rowData = {}
 		rowData["project_id"] = projectId
 		rowData["project_name"] = projectsData[projectId].Appr_Title
 		studentId = projectsData[projectId].Student_Selected
 		#print "studentId:  ", studentId
 		if (studentId != "-1"):
	 		student = studentsData[studentId]
	 		rowData["student_name"] = student.First_Name + " " + student.Last_Name
	 		rowData["student_gpa"] = student.GPA
	 		rowData["primary_major"] = student.Primary_Major
	 		rowData["project_preferance"] = getProjectPreferance(student, projectId)
	 		rowData["req1_satisfied"] = "True"
	 		rowData["req2_satisfied"] = "True"
	 		rowData["req3_satisfied"] = "True"
	 		rowData["skillset_1"] = student.Skills_1
	 		rowData["skillset_2"] = student.Skills_2
	 		rowData["skillset_3"] = student.Skills_3
	 		rowData["studentOption"] = studentListForEachProjectId[projectId]
			
	#		print "\n*****", studentListForEachProjectId[projectId]
	#		print "\nRowData: ",rowData
	 		context.append(rowData)
	 	else:
	 		rowData["student_name"] = ""
	 		rowData["student_gpa"] = ""
	 		rowData["primary_major"] = ""
	 		rowData["project_preferance"] = ""
	 		rowData["req1_satisfied"] = ""
	 		rowData["req2_satisfied"] = ""
	 		rowData["req3_satisfied"] = ""
	 		rowData["skillset_1"] = ""
	 		rowData["skillset_2"] = ""
	 		rowData["skillset_3"] = ""
	 		rowData["studentOption"] = {}
			
			#print "\n*****", studentListForEachProjectId[projectId]
			#print "\nRowData: ",rowData
	 		context.append(rowData)	 		

	print "\n\nContext: ", len(context)
	#print "Context: ", context
 	return context


def getNewStudentToProjectMaps(projectsData, studentsData):
	studentListForEachProjectId = {}

	for projectId in projectsData:
		studentListForEachProjectId[str(projectId)] = []

	for student in studentsData.values():		
		if student.First_Preference != "0" and str(student.Student_Id) not in studentListForEachProjectId[student.First_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.First_Preference]):
			name = str(student.Student_Id)+":"+student.First_Name + " " + student.Last_Name
			d = (str(student.First_Preference)+":"+str(student.Student_Id), name)
			studentListForEachProjectId[str(student.First_Preference)].append(d)
		
		if student.Two_Preference != "0" and  str(student.Student_Id) not in studentListForEachProjectId[student.Two_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.Two_Preference]):
			name = str(student.Student_Id)+":"+student.First_Name + " " + student.Last_Name
			d = (str(student.Two_Preference)+":"+str(student.Student_Id), name)
			studentListForEachProjectId[str(student.Two_Preference)].append(d)
		
		if student.Three_Preference != "0" and  str(student.Student_Id) not in studentListForEachProjectId[student.Three_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.Three_Preference]):
			name = str(student.Student_Id)+":"+student.First_Name + " " + student.Last_Name
			d = (str(student.Three_Preference)+":"+str(student.Student_Id), name)
			studentListForEachProjectId[str(student.Three_Preference)].append(d)
		
		if student.Four_Preference != "0" and  str(student.Student_Id) not in studentListForEachProjectId[student.Four_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.Four_Preference]):
			name = str(student.Student_Id)+":"+student.First_Name + " " + student.Last_Name
			d = (str(student.Four_Preference)+":"+str(student.Student_Id), name)
			studentListForEachProjectId[str(student.Four_Preference)].append(d)
		
		if student.Five_Preference != "0" and str(student.Student_Id) not in studentListForEachProjectId[student.Five_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.Five_Preference]):
			name = str(student.Student_Id)+":"+student.First_Name + " " + student.Last_Name
			d = (str(student.Five_Preference)+":"+str(student.Student_Id), name)
			studentListForEachProjectId[str(student.Five_Preference)].append(d)


	return studentListForEachProjectId


def getProjectPreferance(student, projectId):
	if student.First_Preference == str(projectId):
		return "First" 
	elif student.Two_Preference == str(projectId):
		return "Second"
	elif student.Three_Preference == str(projectId):
		return "Third"
	elif student.Four_Preference == str(projectId):
		return "Fourth"
	elif student.Five_Preference == str(projectId):
		return "Fifth"


def updateDataInDb(projectToStudentMap):
	reverseMap = reverseprojectToStudentMap(projectToStudentMap)
	
	projects = list(ProjectModel.objects.all())
	
	students = list(Student.objects.all())

	for project in projects:
		if project.Id in projectToStudentMap: 
			project.Student_Selected = projectToStudentMap[str(project.Id)]        
			project.save()

	for student in students:
		if str(student.Student_Id) in reverseMap:
			student.Project_selected_for = reverseMap[str(student.Student_Id)]        
			student.save()


def reverseprojectToStudentMap(projectToStudentMap):
	reverseprojectToStudentMap = {}
	for projectId in projectToStudentMap:
		reverseprojectToStudentMap[projectToStudentMap[projectId]] = projectId
	#print "reverseprojectToStudentMap: ", reverseprojectToStudentMap
	return reverseprojectToStudentMap


def removeStudentsWhoDontSatisfyBareMinimumReq(studentsData):
	removeStudentList = []
	for studentId in studentsData:
		student = studentsData[studentId]
		removeFlag = 0
		if student.Degree_Level == "MS":
			removeStudentList.append(studentId)
		elif student.Availability == "0":
			removeStudentList.append(studentId)
		elif student.Got_DLA_Before == "1":
			removeStudentList.append(studentId)
		elif student.Level == "FSE":
			removeStudentList.append(studentId)
		'''elif student.Enrollment  == "1":
			removeStudentList.append(studentId)'''
		#print studentId, student.Degree_Level, student.Availability, student.Got_DLA_Before, student.Level
	
	print "Students who don't meet requirements: ", removeStudentList

	for studentId in removeStudentList:
		del studentsData[studentId]



def removeAssignedStudents(studentListForEachProjectId, projectToStudentMap):
	flag = 0

	for allotedProjectId in projectToStudentMap:
		studentId = projectToStudentMap[allotedProjectId]
		for projectId in studentListForEachProjectId:
			if studentId in studentListForEachProjectId[projectId]:
				studentListForEachProjectId[projectId].remove(studentId)
				flag = 1

	#print "&&&", studentListForEachProjectId
	return flag

def removeAssignedStudents(studentListForEachProjectId, studentId):
	#print "removing...", studentId
	for projectId in studentListForEachProjectId:
		if studentId in studentListForEachProjectId[projectId]:
			studentListForEachProjectId[projectId].remove(studentId)



def removeSelectedStudents(projectsData, studentsData):
	removeProjectIds = {}
	i = 0
	list = []
	for projectId in projectsData:
		#print "Dude", projectId, str(projectsData[projectId].IS_Facutly_Selected),  str(projectsData[projectId].IS_admin_Selected)
		if str(projectsData[projectId].IS_Facutly_Selected) == "1" or str(projectsData[projectId].IS_admin_Selected) == "1":
			removeProjectIds[projectId] = projectsData[projectId].Student_Selected
		i += 1

	for projectId in removeProjectIds:
		if removeProjectIds[projectId] in studentsData:
			del studentsData[removeProjectIds[projectId]]
		if projectId in projectsData:
			del projectsData[projectId]
		list.append(projectId)

	return list


def createProjectDataDictionary(projectData):
	ProjectDataDic = {}
	for project in projectData:
		ProjectDataDic[str(project.Id)] = project
	return ProjectDataDic

def createStudentDataDictionary(studentsData):
	studentsDataDic = {}
	for student in studentsData:
		studentsDataDic[str(student.Student_Id)] = student
	return studentsDataDic



def getStudentToProjectMaps(projectsData, studentsData, removeProjectIdList):
	studentListForEachProjectId = {}

	for projectId in projectsData:
		studentListForEachProjectId[str(projectId)] = []
	#print "___________studentListForEachProjectId:  ", studentListForEachProjectId

	for student in studentsData.values():		
		#print "StudentPreferance: ", str(student.Student_Id), student.First_Preference, student.Two_Preference, student.Three_Preference, student.Four_Preference , student.Five_Preference 
		getStudentListForEachProjectId(student,  projectsData, studentListForEachProjectId, removeProjectIdList)

	return studentListForEachProjectId


def getStudentListForEachProjectId(student, projectsData, studentListForEachProjectId, removeProjectIdList):

	#print "!!!!!!!Idiot", student.Student_Id, student.First_Preference, student.Two_Preference, student.Three_Preference, student.Four_Preference , student.Five_Preference #, (str(student.Student_Id) not in studentListForEachProjectId[student.First_Preference]), (ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.First_Preference]))

	if student.First_Preference != "0" and student.First_Preference not in removeProjectIdList and str(student.Student_Id) not in studentListForEachProjectId[student.First_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.First_Preference]):
		studentListForEachProjectId[str(student.First_Preference)].append(str(student.Student_Id))
		
	if student.Two_Preference != "0" and student.Two_Preference not in removeProjectIdList and str(student.Student_Id) not in studentListForEachProjectId[student.Two_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.Two_Preference]):
		studentListForEachProjectId[str(student.Two_Preference)].append(str(student.Student_Id))
	
	if student.Three_Preference != "0" and student.Three_Preference not in removeProjectIdList and str(student.Student_Id) not in studentListForEachProjectId[student.Three_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.Three_Preference]):
		studentListForEachProjectId[str(student.Three_Preference)].append(str(student.Student_Id))
	
	if student.Four_Preference != "0" and student.Four_Preference not in removeProjectIdList and str(student.Student_Id) not in studentListForEachProjectId[student.Four_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.Four_Preference]):
		studentListForEachProjectId[str(student.Four_Preference)].append(str(student.Student_Id))
	
	if student.Five_Preference != "0" and student.Five_Preference not in removeProjectIdList and str(student.Student_Id) not in studentListForEachProjectId[student.Five_Preference] and ifStudentSatisfyBareMinimumReqOfProject(student, projectsData[student.Five_Preference]):
		studentListForEachProjectId[str(student.Five_Preference)].append(str(student.Student_Id))


def discardProjectsWithZeroStudents(studentListForEachProjectId, projectToStudentMap):
	
	for projectId in studentListForEachProjectId:
		if len(studentListForEachProjectId[projectId]) == 0 and projectId not in projectToStudentMap:
			projectToStudentMap[projectId] = -1

	print "In Zero Discard: ", projectToStudentMap	

def ifStudentSatisfyBareMinimumReqOfProject(student, project):
	flag = True
	#print "$$$",student.Student_Id, student.First_Preference, student.P1_Req1, student.P1_Req2, student.P1_Req3
	#print (project.Requirement1 != "None"), (student.P1_Req1 == "0"), (project.Requirement2 != "None"), (student.P1_Req2 == "0"), (project.Requirement1 != "None"),(student.P1_Req3 == "0")
	if student.First_Preference == str(project.Id):
		if (project.Requirement1 != "None" and student.P1_Req1 == "0") and (project.Requirement2 != "None" and student.P1_Req2 == "0") and (project.Requirement1 != "None" and student.P1_Req3 == "0"):
			return False 
	elif student.Two_Preference == str(project.Id):
		if (project.Requirement1 != "None" and student.P2_Req1 == "0") and (project.Requirement2 != "None" and student.P2_Req2 == "0") and (project.Requirement1 != "None" and student.P2_Req3 == "0"):
			return False
	elif student.Three_Preference == str(project.Id):
		if (project.Requirement1 != "None" and student.P3_Req1 == "0") and (project.Requirement2 != "None" and student.P3_Req2 == "0") and (project.Requirement1 != "None" and student.P3_Req3 == "0"):
			return False
	elif student.Four_Preference == str(project.Id):
		if (project.Requirement1 != "None" and student.P4_Req1 == "0") and (project.Requirement2 != "None" and student.P4_Req2 == "0") and (project.Requirement1 != "None" and student.P4_Req3 == "0"):
			return False
	elif student.Five_Preference == str(project.Id):
		if (project.Requirement1 != "None" and student.P5_Req1 == "0") and (project.Requirement2 != "None" and student.P5_Req2 == "0") and (project.Requirement1 != "None" and student.P5_Req3 == "0"):
			return False

	if student.GPA < project.Min_GPA:
		#print "GPA is less"
		return False

	#print student.Student_Id, project.Id, "Student satisfies Project Requirements: ", flag
	return flag


def matchProjectsWithOneStudents(studentListForEachProjectId, studentsData, projectToStudentMap, projectsData):
	projectLisWithOneStudent = {}
	studentCount = {}

	for projectId in studentListForEachProjectId:

		if len(studentListForEachProjectId[projectId]) == 1:
			studentId = (studentListForEachProjectId[projectId])[0]
			if ifStudentSatisfyBareMinimumReqOfProject(studentsData[studentId], projectsData[projectId]):
				if studentId in projectLisWithOneStudent:
					projectLisWithOneStudent[(studentListForEachProjectId[projectId])[0]].append(projectId)
				else:
					projectLisWithOneStudent[(studentListForEachProjectId[projectId])[0]] = [projectId]

	print "projectLisWithOneStudent: ", projectLisWithOneStudent

	for studentId in projectLisWithOneStudent:
		if len(projectLisWithOneStudent[studentId]) > 1:
			getStudentsPreferenceNumber(studentId, projectLisWithOneStudent[studentId], studentsData, projectToStudentMap)
		else:
			projectToStudentMap[projectLisWithOneStudent[studentId][0]] = studentId

	print "projectToStudentMap: ", projectToStudentMap

def getStudentsPreferenceNumber(studentId, ProjectIds, studentData, projectToStudentMap):
	projectPreferance = {}  #{studentId:preferanceNumber}

	for projectId in ProjectIds:
		student = studentData[studentId]
		#print student.First_Preference, student.Two_Preference, student.Three_Preference, student.Four_Preference, student.Five_Preference
		if student.First_Preference == projectId:
			projectPreferance[projectId] = 1
		elif student.Two_Preference == projectId:
			projectPreferance[projectId] = 2
		elif student.Three_Preference == projectId:
			projectPreferance[projectId] = 3
		elif student.Four_Preference == projectId:
			projectPreferance[projectId] = 4
		elif student.Five_Preference == projectId:
			projectPreferance[projectId] = 5

	#print studentId, projectPreferance

	bestProjectId = getBestPreferanceProject(projectPreferance)
	projectToStudentMap[bestProjectId] = studentId

	for projectId in ProjectIds:
		if projectId not in projectToStudentMap:
			projectToStudentMap[projectId] = -1

		
def getBestPreferanceProject(projectPreferance):
	bestProjectId = 0
	rank = 6
	
	for projectId in projectPreferance:
		#print rank, projectPreferance[projectId], projectId, (rank > projectPreferance[projectId])
		if rank > projectPreferance[projectId]:
			bestProjectId = projectId
			rank = projectPreferance[projectId]
			#print bestProjectId
	#print "\n bestProject: ", bestProjectId
	return bestProjectId


def matchProjectsWithMoreThanOneStudents(studentListForEachProjectId, studentsData, projectToStudentMap):
	studentIdToScore = {}

	for projectId in studentListForEachProjectId:
		if projectId not in projectToStudentMap:
			studentIdToScore = {}
			print "\n\nstarting for project Id: ", projectId
			print "studentListForEachProjectId:  ", studentListForEachProjectId[projectId]
			
			for studentId in studentListForEachProjectId[projectId]:
				studentIdToScore[studentId] = getStudentScore(studentsData[studentId], projectId)

			projectToStudentMap[projectId] = getBestScoreStudentId(studentIdToScore, studentsData)
			removeAssignedStudents(studentListForEachProjectId, projectToStudentMap[projectId])
			discardProjectsWithZeroStudents(studentListForEachProjectId, projectToStudentMap)
			print "projectToStudentMap:  ", projectToStudentMap


def getBestScoreStudentId(studentIdToScore, studentsData):
	
	bestScore = 0
	studentIds = []
	print "StudentScores: ", studentIdToScore
	for studentId in studentIdToScore:
	#	print studentIdToScore[studentId], bestScore, (studentIdToScore[studentId] > bestScore)
		if studentIdToScore[studentId] > bestScore:
			bestScore = studentIdToScore[studentId]
			studentIds = [studentId]
		elif studentIdToScore[studentId] == bestScore:
			studentIds.append(studentId)
	#print "bestScore: ", bestScore, studentIds
	if len(studentIds) == 1:
		return studentIds[0]
	else:
		return tieBreaker(studentIds, studentsData)



def getStudentScore(student, projectId):	
	#print "Student Data: ", student.Student_Id, student.Previous_Research, student.Applied_Before, student.Level, student.Gender, student.Race, student.GPA
	score = 0
	if student.Previous_Research == "1":
		score +=1

	if student.Applied_Before == "1":
		score +=1

	if student.Level == "F":
		score +=1
	elif student.Level == "SO":
		score +=2
	elif student.Level == "J":
		score +=3
	elif student.Level == "SE":
		score +=4
	
	if student.First_Preference == projectId:
		score += 5
	elif student.Two_Preference == projectId:
		score += 4
	elif student.Three_Preference == projectId:
		score += 3
	elif student.Four_Preference == projectId:
		score += 2
	elif student.Five_Preference == projectId:
		score += 1
	return score


def tieBreaker(studentIds, studentData):
	#print "IN tieBreaker..."
	studentTieBreakerScore = {}
	
	for studentId in studentIds:
		student = studentData[studentId]
		score = 0
		if student.Gender == "F":
			score +=2
		elif student.Gender == "M":
			score +=1

		if student.Race == "AI_AN":
			score +=1
		elif student.Race == "B_AA":
			score +=1
		elif student.Race =="NH_OPI":
			score +=1
		studentTieBreakerScore[studentId] = score

	bestScore = 0
	studentTieIds = []

	#print "studentTieBreakerScore:  ", studentTieBreakerScore

	for studentId in studentTieBreakerScore:
		if studentTieBreakerScore[studentId] > bestScore:
			studentTieIds = [studentId]
		elif studentTieBreakerScore[studentId] == bestScore:
			studentTieIds.append(studentId)
	
	#print "studentTieIds:   ", studentTieIds

	if len(studentTieIds) == 1:
		return studentTieIds[0]
	else:
		bestGpa = 0
		bestStudent = 0
		for studentId in studentTieIds:
			if studentData[studentId].GPA > bestGpa:
				bestGpa = studentData[studentId].GPA
				bestStudent = studentId
		return bestStudent
  
def matrixtoxcel():

    projects = list(ProjectModel.objects.all())
    students = list(Student.objects.all())
    projlen = len(projects)
    studlen = len(students)
    labels = ["Student Name", "Primary Major", "Level in school", "GPA", "Gender", "Ethinicity", "Prev Exp", "Applied Before"]
    extras = len(labels)
    for i in projects:
        labels.append(i.Appr_Title)
    print labels
    
    values = [ ["" for j in range(len(students))] for j in range(len(labels))]
    
    print "rows =", len(values)
    print "cols =", len(values[0])
        
    
    rowct = 0

    for stud in students:            
        colct = extras
                
        for proj in projects:

            projectId = proj.Id
            cell = []
            if (stud.First_Preference == str(projectId)):
			cell.append("1")
            if (stud.Two_Preference == str(projectId)):
			cell.append("2")
            if (stud.Three_Preference == str(projectId)):
			cell.append("3")
            if (stud.Four_Preference == str(projectId)):
			cell.append("4")
            if (stud.Five_Preference == str(projectId)):
			cell.append("5")
            #print rowct, colct, "\n"

            if cell != []:                
                values[colct][rowct] = ', '.join(cell)               
            
            colct = colct + 1
            
        rowct = rowct + 1  
    
    
    for i in range(studlen):
        stud = students[i]
        values[0][i] = stud.First_Name + " ".decode("utf-8") + stud.Last_Name
        values[1][i] = stud.Primary_Major
        values[2][i] = stud.Level
        values[3][i] = stud.GPA
        values[4][i] = stud.Gender
        values[5][i] = stud.Race
        values[6][i] = stud.Previous_Research
        values[7][i] = stud.Applied_Before
    #print labels
    #print values
    
    nac = {}
    
    ct = 0
    for i in labels:
        nac[i] = values[ct]
        print i
        print values[ct]
        ct = ct + 1
    
    df = pd.DataFrame(nac)
    #print df
    df.to_excel('personal/static/personal/test.xlsx', sheet_name='sheet1', index=False)
    #print values
    