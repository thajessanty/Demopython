from django.http import HttpResponse
from django.shortcuts import render
from.models import Place,myteam

# Create your views here.
def cars(request):
    obj=Place.objects.all()
    team=myteam.objects.all()
    return render(request,"index.html",{'result':obj,'result2':team})

# #def home(request):
#     return render(request,'home.html')
#
# #def about(request):
#     return render(request,'about.html')
#
# #def contact(request):
#     return render(request,'contact.html')
#
# #def detail(request):
#     return render(request,'detail.html')

#def thanks(request):
#     return HttpResponse('thank you for watching')
# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     multi = x * y
#     sub = x - y
#     div = x / y
#
#
#     return render(request,"result.html",{'addition':add,'multiplication':multi,'subtraction':sub,'division':div})



