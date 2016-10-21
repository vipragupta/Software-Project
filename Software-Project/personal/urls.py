from django.conf.urls import url, include
from . import views
from views import index
from django.contrib.auth import login, logout
#from personal.forms import LoginForm
from django.contrib import admin

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^home$', views.home, name='home'),
	url(r'^login$', views.login , name='login'),
	url(r'^studenthome$', views.studenthome , name='studenthome'),
	url(r'^facultyhome$', views.facultyhome , name='facultyhome'),
	url(r'^projects$', views.projects , name='projects'),
	url(r'^addprojects$', views.addprojects , name='addprojects'),
	
	#user auth urls
	url(r'^accounts/login/$', views.login),
	url(r'accounts/auth/$', views.auth_view),
	url(r'accounts/logout/$', views.logout),
	url(r'accounts/loggedin/$', views.loggedin),
	url(r'accounts/invalid/$', views.invalid_login),

]