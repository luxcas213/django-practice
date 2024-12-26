from django.shortcuts import render,redirect
from django.http import HttpResponse , JsonResponse
from .models import task,project
from django.shortcuts import get_object_or_404
from .forms import createnewtask
# Create your views here.
def index(request):
    title="My First Django Project"
    return render(request, "index.html", {"title": title})



def hello(request, id):
    print(id)
    return HttpResponse("<h1>Hello %s</h1>"% id)

def about(request):
    return render(request, "about.html")

def projects(request):
    
    # p=list(project.objects.values())
    p=project.objects.all()
    return render(request, "projects.html",{
        "projects":p
    })

def tasks(request):
    t=task.objects.all()
    print(t)
    return render(request, "task.html",{
        "tasks":t
    })

def createtask(request):
    if request.method=="GET":
        return render(request, "create_task.html",{"form":createnewtask()})
    else:
        task.objects.create(title=request.POST["title"],description=request.POST["description"],project_id=1)
        return redirect("/task/")