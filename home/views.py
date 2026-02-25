from django.shortcuts import render, redirect
from .models import Project, Skill, Contact

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        "projects": projects,
        "skills": skills,
        "name": "Mohammad Hasrat",
        "role": "Full-Stack Python & Django Developer",
        "about": "I am a dedicated BCA student and passionate full-stack web developer specializing in Python, Django, and MySQL.",
    }
    return render(request, "index.html", context)


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            message=request.POST["message"]
        )
        return redirect("/success/")
    return render(request, "contact.html")


def success(request):
    return render(request, "success.html")