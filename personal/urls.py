from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^response', views.post_response2),
    url(r'^$', views.post_create),
]
