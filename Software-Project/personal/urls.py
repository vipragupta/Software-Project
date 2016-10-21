from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
	url(r'^login$', views.login , name='login'),
	url(r'^studenthome$', views.studenthome , name='studenthome'),
	url(r'^facultyhome$', views.facultyhome , name='facultyhome'),
	url(r'^projects$', views.projects , name='projects'),
	url(r'^addprojects$', views.addprojects , name='addprojects'),
]
