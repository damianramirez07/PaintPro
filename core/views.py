from django.shortcuts import render

# Main Dashboard
def dashboard(request):
    return render(request, 'core/dashboard.html')

