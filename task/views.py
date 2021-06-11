from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm



# Create your views here.
def index(request):
    
    tasks = Task.objects.all()
    
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'task/home.html', {'tasks':tasks,'form':form})

def editTask(request,pk):
    
    task = Task.objects.get(pk=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'task/edit_task.html',{'form':form})

def deleteTask(request,pk):

    chosentask = Task.objects.get(pk=pk)
    
    if request.method == 'POST':
        chosentask.delete()
        return redirect('/')

    return render(request, 'task/delete_task.html', {'task':chosentask})