from django.conf.urls import url
from django.urls import path
from . import views
from django.utils import timezone
import requests

urlpatterns = [
    url(r'^main_tasks$', views.main_tasks, name='main_tasks'),
    url(r'^add_task$', views.add_task, name='add_task'),
    url(r'^main_tasks$', views.check_task, name='check_task'),
    url(r'^signup', views.create_user, name='signup'),
    url(r'^logout', views.logoutuser, name='logout'),
    url(r'^', views.auth_user, name='login')
]