from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number', 'first_name', 'last_name', 'address', 'mobile_number','photo']

