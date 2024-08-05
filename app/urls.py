from django.urls import path
from .views import *

urlpatterns = [
  path('',home,name="home"),
  path('profile/',profile,name="profile"),

  path('certificate-form/', education_form, name='create'),
  path('get-subjects/<int:certificate_id>/', get_subjects, name='get_subjects'),
 
  path('register/',register,name="register"),
  path('login/',loginPage,name="login"),
  path('logout/',logoutPage,name="logout"),

  path('delete/<int:pk>/', delete, name='delete'),
]