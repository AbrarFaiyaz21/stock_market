from django.shortcuts import render
from .models import JSONData

# Create your views here.

def home(request):
    data = JSONData.objects.all()
    return render(request, 'myapp/home.html', {'data': data})