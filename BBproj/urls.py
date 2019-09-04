
# Create your views here.
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$' , views.home, name = 'homescreen'),
    url(r'^home/$' , views.loggedin, name = 'loggedin'),
    url(r'^timestamp/$' , views.timestamp, name = 'timestamp'),
url(r'^assignwork/$' , views.assignwork, name = 'assignwork'),
url(r'^assigned_work/$' , views.assignedwork, name = 'assignedwork'),
url(r'^loggout/$' , views.loggout, name = 'loggout'),
# url(r'^work/(?P<text_id>[0-9]+)/$', views.text_append, name=''),
url(r'^work/$' , views.work, name = 'work'),
]
