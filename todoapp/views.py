from django.http import HttpResponse
from django.template import loader
from .models import Todo
from django.shortcuts import render, redirect


def index(req):
    todo = Todo.objects.all()
    context = {"todo": todo}
    return render(req, "index.html", context)


def create(req):
    if req.method == "POST":
        title = req.POST.get("title")
        desc = req.POST.get("desc")

        Todo.objects.create(title=title, desc=desc)
        return redirect("/todoapp")
    return render(req, "create.html")


def edit(req, id):
    todo = Todo.objects.get(id=id)

    if req.method == "POST":
        title = req.POST.get("title")
        desc = req.POST.get("desc")

        todo.title = title
        todo.desc = desc

        todo.save()
        return redirect("/todoapp")
    context = {"todo": todo}
    return render(req, "edit.html", context)


def delete(req, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/todoapp")
