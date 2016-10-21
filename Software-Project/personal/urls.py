from django.conf.urls import url, include
from . import views
#from views import index
from django.contrib.auth import login, logout
#from personal.forms import LoginForm
from django.contrib import admin

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^home$', views.home, name='home'),
#	url(r'^login$', views.login , name='login'),
	url(r'^studenthome$', views.studenthome , name='studenthome'),
	url(r'^facultyhome$', views.facultyhome , name='facultyhome'),
	url(r'^projects$', views.projects , name='projects'),
	url(r'^addprojects$', views.addprojects , name='addprojects'),
	
	#user auth urls
	#url(r'^accounts/login/$', views.login),
	#url(r'accounts/auth/$', views.auth_view),
	#url(r'accounts/logout/$', views.logout),
	#url(r'accounts/loggedin/$', views.loggedin),
	#url(r'accounts/invalid/$', views.invalid_login),

	#user auth urls
	url(r'^login_faculty$', views.login_faculty, name='login_faculty'),
	url(r'^login_student$', views.login_student, name='login_student'),
	url(r'^auth_faculty$', views.auth_view_faculty, name='auth_faculty'),
	url(r'^auth_student$', views.auth_view_student, name='auth_student'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^loggedin$', views.loggedin, name='loggedin'),
	url(r'^invalid$', views.invalid_login, name='invalid_login'),
]