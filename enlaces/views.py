from django.shortcuts import render
from .models import Enlace

# Create your views here.
def enlaces(request):
    enlaces = Enlace.objects.all()
    return render(request, "home.html", {"enlaces": enlaces})