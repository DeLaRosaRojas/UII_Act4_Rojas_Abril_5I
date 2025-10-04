from django.shortcuts import render

# Create your views here.
def index(request):
    clientes = [
        {
            'nombre': 'Ana Torres',
            'email': 'ana.torres@example.com',
            'telefono': '555-1234'
        },
        {
            'nombre': 'Carlos Ruiz',
            'email': 'carlos.ruiz@example.com',
            'telefono': '555-5678'
        },
        {
            'nombre': 'Marta Soler',
            'email': 'marta.soler@example.com',
            'telefono': '555-9012'
        },
    ]
    contexto = {
        'clientes': clientes
    }
    return render(request, 'index.html', contexto)