from sqlite3 import Timestamp
from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    allProj = Project.objects.order_by('TimeStamp')
    context = {'allProj': allProj}
    return render(request, 'projects/home.html', context)

def project(request, Slug):
    proj = Project.objects.filter(Slug=Slug).first()
    context = {'proj':proj}
    return render(request, 'projects/project.html', context)

def searchProject(request):
    query = request.GET['query']
    if len(query) > 50:
        searchResults=Project.objects.none()
    else:
        searchProjTitle=Project.objects.filter(Title__icontains=query)
        searchProjBody=Project.objects.filter(Body__icontains=query)
        searchResults=searchProjTitle.union(searchProjBody)
    context={'searchResults':searchResults, 'query':query}
    return render(request, 'projects/search.html', context)