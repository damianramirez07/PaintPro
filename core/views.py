from django.shortcuts import render
from .models import Project

# Main Dashboard
def dashboard(request):
    projects = Project.objects.all() # Grab all the projects in the DB

    return render(request, 'core/dashboard.html', {
        'projects': projects 

    })



