#created by mee! deepak
from django.urls import path
from user_app import views

#TEMPLATES URL
app_name = 'user_app'

urlpatterns= [
    path('register/',views.register, name = 'register')
]