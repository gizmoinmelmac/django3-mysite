from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    template_name = 'portfolio/home.html'
    context = {}
    return render(request, 'portfolio/home.html', {'projects': projects})
