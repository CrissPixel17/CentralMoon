from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from gestionVideojuegos.models import Videojuegos, Consola

def inicio(request):
    return render(request,"inicio.html",{"proyecto":"Mi Proyecto"})

def videojuegos(request):
    juegos = Videojuegos.objects.all()  # Obtén todos los juegos de la base de datos
    return render(request, "videojuegos.html", {"juegos": juegos})


def consolas(request):
    consolas = Consola.objects.all()
    return render(request,"consola.html",{"consolas": consolas})

def buscar_consolas(request):
    query = request.GET.get("sbd","").strip()
    mensaje = None
    imagen_error = None
    consolas = []

    if query:
        consolas = Consola.objects.filter(nombre__icontains=query)
        if not consolas:
            mensaje = "Consola no encontrada o no existe"
            imagen_error = "/media/mensaje_error/nosep.png"
    else:
        mensaje = "No has ingresado ningun valor"
        imagen_error = "/media/mensaje_error/robot.png"
    return render(request, "consola.html", {
        "consolas": consolas,
        "mensaje": mensaje,
        "imagen_error": imagen_error
    })

def buscar(request):
    query = request.GET.get("prd", "").strip()  # Obtiene el valor y elimina espacios en blanco
    mensaje = None  # Variable para manejar los mensajes de error
    imagen_error = None  # Imagen a mostrar en caso de error
    juegos = []  # Lista vacía si no hay resultados

    if query:  # Verifica si se ingresó algo en el buscador
        juegos = Videojuegos.objects.filter(titulo__icontains=query)
        if not juegos:
            mensaje = "Juego no encontrado o no existe."
            imagen_error = "/media/mensaje_error/nosep.png"
    else:
        mensaje = "No has ingresado ningún valor."
        imagen_error = "/media/mensaje_error/robot.png"

    return render(request, "videojuegos.html", {
        "juegos": juegos,
        "mensaje": mensaje,
        "imagen_error": imagen_error
    })


def formulario(request):
    if request.method=="POST":
        subject = request.POST["asunto"]

        message = request.POST["mensaje"]+" "+request.POST["email"]

        email_from = settings.EMAIL_HOST_USER

        recipient_list = ["crisspixel17@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request,"gracias.html")
    
    return render(request,"formulario.html")
