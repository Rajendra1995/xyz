from django.urls import path
from . import views

urlpatterns = [
    path('homepage/<int:id>', views.homePage),  # http://127.0.0.1:8000/homepage
    path('aboutus', views.aboutUs), #http://127.0.0.1:8000/aboutus
    path('studentform', views.student_form) #http://127.0.0.1:8000/studentform
]
