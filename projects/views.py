from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all() # fetching all the objects created
    context = {
        # Django uses the context dictionary to send information to your template.
        "projects": projects
    }
    # Any entries in the context dictionary are available in the template, as long as you pass the context argument to render()
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)  # grab a project by the primary key equal to function argument
    context = {
        # Django uses the context dictionary to send information to your template.
        "project": project
    }
    return render(request, "projects/project_detail.html", context)
