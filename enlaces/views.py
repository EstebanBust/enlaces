from django.shortcuts import render
from .models import Enlace, MyUser
from django.contrib.auth.models import User

# Create your views here.
def enlaces(request):
    enlaces = Enlace.objects.all()
    return render(request, "home.html", {"enlaces": enlaces})

def create_superuser(request):
    # Crea el usuario
    user = User.objects.create_superuser(
        username='Luktor',
        password='1n-o$XK>u7l@hK0',
        email='esteban.bustamante.c@gmail.com'
    )

    # Crea la instancia de MyUser asociada al usuario
    myuser = MyUser.objects.create(user=user)

    # Agrega cualquier otra configuración que desees para el usuario aquí

    # Renderiza una respuesta para indicar que el usuario ha sido creado exitosamente
    return render(request, 'create_superuser.html')