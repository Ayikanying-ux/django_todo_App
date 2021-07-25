from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    task = AddTask.objects.all()
    form = TaskForm
    context ={'task': task, 'form': form}
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "base/index.html", context)


def update(request, pk):
    task = AddTask.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}

    return render(request, "base/update.html", context)

def delete(request, pk):
    item = AddTask.objects.get(id=pk)

    item.delete()
    return redirect("/")