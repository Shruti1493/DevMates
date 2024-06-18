
from django.contrib import admin
from django.urls import path,include
from projects.views import *

urlpatterns = [
    path('create/', CreateUserProject.as_view(), name ='create project'),
    


   

]
