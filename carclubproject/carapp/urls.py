from .import views
from django.urls import path

urlpatterns = [

    path('', views.cars, name='cars'),
    #path('home/',views.home,name='home'),
    #path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='contact'),
    #path('detail/',views.detail,name='details'),
    #path('thanks/',views.thanks,name='thanks'),
    #path('operation/',views.operation,name='operation'),



]