from django.http import HttpResponse

# Main Dashboard
def dashboard(request):
    return HttpResponse("Welcome to PaintPro - Painting Project Management") 
