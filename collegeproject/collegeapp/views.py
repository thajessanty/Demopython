from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from collegeapp.forms import Order
import json
from collegeapp.models import Teacher,Department,Course,Gender,Purpose,Materials


def demo(request):

    obj = Teacher.objects.all()

    return render(request, "about.html", {'result': obj})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            form = Order()
            return render(request, 'registration.html', {'form': form})

        else:
            message = 'User not registerd'
            return render(request, 'login.html', {'message': message})

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password != cpassword:
            error_message = 'Passwords do not match'
            return render(request, "register.html", {'error_message': error_message})
        else:
            if User.objects.filter(username=username).exists():
                error_message = 'Username is already taken'
                return render(request, "register.html", {'error_message': error_message})
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                success_message = 'User created successfully!'
                return render(request, "login.html", {'success_message': success_message})
    else:
        return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('collegeapp:login')


def registration(request):
    form = Order(request.POST, request=request)  # Pass 'request' as an additional argument
    order_s_message = False

    if request.method == "POST":
        form = Order(request.POST, request=request)  # Pass 'request' as an additional argument
        if form.is_valid():
            form.save()
            order_s_message = True
            return redirect('collegeapp:success_page')

    return render(request, 'registration.html', {'form': form, 'order_confirmed': order_s_message})


def success_page(request):
    return render(request, "success_page.html")

def getCourses(request):
    print('getCourses view called')
    data = json.loads(request.body)
    print('Received data:', data)
    data= json.loads(request.body)
    department_id= data['id']
    courses=Course.objects.filter(department__id=department_id)
    print(department_id)
    return JsonResponse(list(courses.values("id", "name")), safe=False)
















































