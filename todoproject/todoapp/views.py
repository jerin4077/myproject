from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import ToDo
from .forms import ToDoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskListView(ListView):
    model=ToDo
    template_name = 'home.html'
    context_object_name = 'todo'

class TaskDetailView(DetailView):
    model=ToDo
    template_name = 'details.html'
    context_object_name = 'todo'

class TaskUpdateView(UpdateView):
    model = ToDo
    template_name = 'update.html'
    context_object_name = 'todo'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailview/',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = ToDo
    template_name = 'delete.html'
    success_url = reverse_lazy('listview/')









def add_task(request):
    task1 = ToDo.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        todo=ToDo(name=name,priority=priority,date=date)
        todo.save()
    return render(request,"home.html",{'todo':task1})
def delete(request,taskid):
    task=ToDo.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,taskid):
    task=ToDo.objects.get(id=taskid)
    form=ToDoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})

# Create your views here.
