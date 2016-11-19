from django.conf.urls import url, include
from . import views
from django.contrib.auth import login, logout
from django.contrib import admin

#All the urls in the project are written below
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	
	#Home Page URL
	url(r'^home$', views.home, name='home'),
	
	#Faculty Page URLs
	url(r'^facultyhome$', views.facultyhome , name='facultyhome'),
	url(r'^projects/$', views.projects , name='projects'),
	url(r'^rawmatrix/$', views.rawmatrix , name='rawmatrix'),
	url(r'^projects/(?P<pid>\d+)$', views.project, name='project' ),
	url(r'^addprojects/$', views.addprojects , name='addprojects'),
	
	#Student Page URLs
	url(r'^studenthome$', views.studenthome , name='studenthome'),
	url(r'^viewprojects$', views.viewprojects , name='viewprojects'),
	url(r'^applyprojects$', views.applyprojects , name='applyprojects'),
	url(r'^updateRequirement.html/(?P<sid>\d+)$', views.updateRequirements, name='updateRequirements' ),
	
	#Login Page and Authentication URLs
	url(r'^login_faculty$', views.login_faculty, name='login_faculty'),
	url(r'^login_student$', views.login_student, name='login_student'),
	url(r'^auth_faculty$', views.auth_view_faculty, name='auth_faculty'),
	url(r'^auth_student$', views.auth_view_student, name='auth_student'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^loggedin$', views.loggedin, name='loggedin'),
	url(r'^invalid$', views.invalid_login, name='invalid_login'),
]