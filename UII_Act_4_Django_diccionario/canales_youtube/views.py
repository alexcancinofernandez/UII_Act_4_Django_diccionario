from django.shortcuts import render

def mostrar_datos(request):
    canales_youtube = [
        {"nombre": "Empresa Tech", "suscriptores": 12000, "categoria": "Tecnología"},
        {"nombre": "Negocios Éxito", "suscriptores": 8500, "categoria": "Emprendimiento"},
        {"nombre": "Vida Saludable MX", "suscriptores": 4300, "categoria": "Salud y Bienestar"},
    ]
    return render(request, 'index.html', {"canales": canales_youtube})

