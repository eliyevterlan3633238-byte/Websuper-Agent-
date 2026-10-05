from django.shortcuts import render, get_object_or_404
from .models import Project, Category

def index(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'categories': categories})

def detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/portfolio_detail.html', {'project': project})
