from django.shortcuts import render , redirect
from .models import coures
from .forms import CourseForm
# Create your views here.
def all_courese(request):
    courese = coures.objects.all()
    return render(request , 'all_courese.html', {'all':courese})

def single(request , id):
    courese = coures.objects.get(id = id)
    return render(request,'single.html',{'single':courese})

def new_courese(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()
    return render(request,'new.html',{'new':form})

def edit(request,id):
    courese = coures.objects.get(id = id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance= courese)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm(instance=courese)
    return render(request,'edit.html',{'edit':form})

def delete(request, id):
    courese = coures.objects.get(id = id)
    courese.delete()
    return redirect('/blog/')