from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    events = MLSAProgram.objects.all()
    
    context = {'events': events}
    
    return render(request, "base/index.html", context)
    