
from django.conf.urls import url
from . import views#importing locally from package

urlpatterns = [
    url(r'^$', views.index, name='index'),]

