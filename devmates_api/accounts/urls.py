from django.contrib import admin
from django.urls import path,include
from accounts.views import *
urlpatterns = [
    path('reg/', UserRegistrationView.as_view(), name ='register'),
    
    path('login/', UserLoginView.as_view(), name ='login'),
    path('profile/', UserProfileView.as_view(), name ='profile'),

   

]
