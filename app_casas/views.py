from django.shortcuts import render, redirect, get_object_or_404
from .models import Casa

# Listar casas
def index(request):
    casas = Casa.objects.all()
    return render(request, 'listar_casas.html', {'casas': casas})

# Ver casa (opcional, puedes usarlo si quieres detalle)
def ver_casa(request, id):
    casa = get_object_or_404(Casa, id=id)
    # Si quisieras una plantilla 'ver_casa.html', la renderizarías aquí
    # return render(request, 'ver_casa.html', {'casa': casa})
    # Por ahora, simplemente redirigimos o mostramos el listado
    return redirect('inicio') # O puedes crear un template para ver una casa individual

# Agregar casa
def agregar_casa(request):
    if request.method == 'POST':
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']
        precio = request.POST['precio']
        estado = request.POST['estado']
        habitaciones = request.POST['habitaciones']
        Casa.objects.create(
            direccion=direccion,
            ciudad=ciudad,
            precio=precio,
            estado=estado,
            habitaciones=habitaciones
        )
        return redirect('inicio')
    return render(request, 'agregar_casa.html')

# Editar casa
def editar_casa(request, id):
    casa = get_object_or_404(Casa, id=id)
    if request.method == 'POST':
        casa.direccion = request.POST['direccion']
        casa.ciudad = request.POST['ciudad']
        casa.precio = request.POST['precio']
        casa.estado = request.POST['estado']
        casa.habitaciones = request.POST['habitaciones']
        casa.save()
        return redirect('inicio')
    return render(request, 'editar_casa.html', {'casa': casa})

# Borrar casa
def borrar_casa(request, id):
    casa = get_object_or_404(Casa, id=id)
    if request.method == 'POST':
        casa.delete()
        return redirect('inicio')
    return render(request, 'borrar_casa.html', {'casa': casa})
# Create your views here.
