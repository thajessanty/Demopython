from . import views
from django.urls import path
app_name='collegeapp'

urlpatterns = [

    path('',views.demo,name='demo'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout,name='logout'),
    path('registration/', views.registration, name='registration'),
    path('course/', views.getCourses, name='getcourses'),
    path('success/', views.success_page, name='success_page'),


]