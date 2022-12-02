from .models import University, Student
from django.forms import ModelForm


class UniversityForm(ModelForm):

    class Meta:
        model = University
        fields = ('full_name', 'short_name', 'established')


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'birth_date', 'university', 'admission_year')
