from django.contrib import admin
from django.urls import path,include
from .import views
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .views import home
app_name='minor'

urlpatterns = [path('',view=views.home,name='home'),
path('teacher',view=views.teacher,name='teacher'),
path('<id>/',view=views.upv,name='upvote'),
path('admin/', admin.site.urls,name='admin'),
#path('/student',view=views.student,name='home'),
               ]


