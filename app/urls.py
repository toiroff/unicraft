from django.urls import path
from .views import home,register,loginPage,profile,create,logoutPage,delete,update

urlpatterns = [
  path('',home,name="home"),
  path('profile/',profile,name="profile"),
  path('create/',create,name="create"),

  path('register/',register,name="register"),
  path('login/',loginPage,name="login"),
  path('logout/',logoutPage,name="logout"),

  path('delete/<str:pk>/',delete,name="delete"),
  path('update/<str:pk>/',update,name="update")
]