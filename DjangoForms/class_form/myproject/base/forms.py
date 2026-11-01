from django import forms
from .models import StudentModel

class StudentForm(forms.Form):
    name = forms.CharField()
    number = forms.IntegerField()
    email = forms.EmailField()
    
    def save(self):
        return StudentModel.objects.create(
            name = self.cleaned_data['name'],
            phone = self.cleaned_data['number'],
            email = self.cleaned_data['email']
        )
        
    def update(self,student):
        student.name = self.cleaned_data['name']
        student.phone = self.cleaned_data['number']
        student.email = self.cleaned_data['email']
        student.save()