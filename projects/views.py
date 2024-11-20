from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Projects.objects.all() # fetching all the objects created
    context = {
        # Django uses the context dictionary to send information to your template.
        "projects": projects
    }
    # Any entries in the context dictionary are available in the template, as long as you pass the context argument to render()
    return render(request, "projects/projects_index.html", context)
