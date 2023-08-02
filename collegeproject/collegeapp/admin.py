from django.contrib import admin
from . models import Teacher,Course,Department,Gender,Materials,Purpose,MyModel

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Gender)
admin.site.register(Purpose)
admin.site.register(Materials)
admin.site.register(MyModel)

