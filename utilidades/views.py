from django.shortcuts import render

# Create your views here.

def error_404_view(request):
    return render(request, '404.html')