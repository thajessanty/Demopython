from django import forms
from django.forms import ModelForm, DateInput, CheckboxSelectMultiple
from collegeapp.models import Department,Course,Materials,MyModel,Teacher



class Order(forms.ModelForm):
    class Meta:
        model=MyModel
        fields="__all__"
        widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
            'materials_provided': CheckboxSelectMultiple(),
        }

    def __init__(self, data=None, request=None, *args, **kwargs):
        super(Order, self).__init__(data=data, *args, **kwargs)
        self.request = request

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('id_department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
