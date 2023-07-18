from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description= models.TextField()
    def __str__(self):
        return self.name

class myteam(models.Model):
    person_name = models.CharField(max_length=250)
    person_image = models.ImageField(upload_to='myteampicture')
    designation = models.TextField()

    def __str__(self):
        return self.person_name