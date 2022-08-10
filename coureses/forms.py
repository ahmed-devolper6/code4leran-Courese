from csv import field_size_limit
from django import forms
from .models import coures
class CourseForm(forms.ModelForm):
    class Meta:
        model = coures
        fields = ['title' , 'contant' , 'price']