from csv import field_size_limit
from django import forms
from .models import coures
class CourseForm(forms.modelform):
    class Meta:
        model = coures
        fields = ['title' , 'contant' , 'price']