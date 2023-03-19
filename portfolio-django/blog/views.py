from django.shortcuts import render
from .models import *

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects':projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project':project})