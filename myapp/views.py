from django.http import HttpResponse, JsonResponse
from .models import project, task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import createnewtask, createnewproject


# Create your views here.
def index(request):
    title = "django course"
    return render(request, "index.html", {"title": title})


def hello(request, username):
    return HttpResponse("<h1>hola %s</h1>" % username)


def about(request):
    username = "yonaM"
    return render(request, "about.html", {"username": username})


def projects(request):
    # projects = list(project.objects.values())
    projects = project.objects.all()
    return render(request, "project/projects.html", {"projects": projects})


def tasks(request):
    # Task = get_object_or_404(task, id=id)
    tasks = task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})


def create(request):
    if request.method == "GET":
        return render(request, "tasks/create.html", {"form": createnewtask})
    else:
        task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        return redirect("tasks")


def create_project(request):
    if request.method == "GET":
        return render(
            request, "project/create_project.html", {"form": createnewproject()}
        )
    else:
        project.objects.create(namme=request.POST["name"])
        redirect("projects")


def project_detail(request, id):
    projects = get_object_or_404(project, id=id)
    tasks = task.objects.filter(project_id=id)
    return render(
        request, "project/detail.html", {"project": projects}, {"tasks": tasks}
    )
