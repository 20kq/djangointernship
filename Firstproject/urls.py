"""Firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('ht/',views.htmltag),
    path('usr/<str:uname>/',views.usernameprint),
    path('userage/<str:name>/<int:age>/',views.uage),
    path('emp/<str:eid>/<int:eage>/<str:ename>/',views.employee),
    path('qw/',views.html),
    path('yt/<str:name>/',views.ytname),
    path('pt/<int:id>/<str:ename>/',views.nameid),
    path('stud/',views.studentdetails),
    path('internaljs/',views.internaljs),
    path('myform/',views.myform,name='myform'),
    path('teja/',views.teja,name='teja'),
    path('task/',views.task,name='task'),
    path('btrstr/',views.bootstrapfun),    
    path('tej/',views.tej,name='tej'),
    path('registration/',views.registration),
    path('registration1/',views.registration1,name='registration1'),
    path('display/',views.display,name="dt"),
    path('viw/<int:y>/',views.sview,name="sv"),
    path('update/<int:q>/',views.supd,name="sup"),
    path('dl/<int:p>/',views.sudl,name="sd"),

]    
