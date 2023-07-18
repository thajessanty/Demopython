from django.http import HttpResponse
from django.shortcuts import render
from .models import place, myteam


# Create your views here.
def demo1(request):
    obj=place.objects.all()
    team = myteam.objects.all()
    return render(request,"index.html",{'result':obj,'result2':team})

#def addition(request):
    x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #return render(request, "about.html",{'result':res})