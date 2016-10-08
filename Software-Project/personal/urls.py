from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^home$', views.page2 , name='page2'),
]
