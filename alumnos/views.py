from django.shortcuts import render
from .models import Alumno
# Create your views here.

def index(request):
    alumnos= Alumno.objects.all()
    context={}
    return render(request,'alumnos/index.html',context)

