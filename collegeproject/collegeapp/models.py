from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Teacher(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='teacher')
    desc = models.TextField()

    class Meta:
        verbose_name_plural = 'teachers'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender

class Purpose(models.Model):
    purpose = models.CharField(max_length=20)

    def __str__(self):
        return self.purpose

class Materials(models.Model):
    materials_provided = models.CharField(max_length=200)

    def __str__(self):
        return self.materials_provided

class MyModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    materials_provided = models.ManyToManyField(Materials)



