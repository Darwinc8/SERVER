from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator 
from .models import Portador
from .forms import PortadorForm
from armamento.forms import BusquedaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def portadores(request):
    portador = Portador.objects.all().order_by('NOMBRE')
    query = request.GET.get('query')
    if query:
        portador = portador.filter(CUIP__icontains=query)
    paginator = Paginator(portador, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'portadores.html', {
        'portadores': page_obj,
        'form': BusquedaForm()
    }) 

@login_required    
def crear_portador(request):
    if request.method == 'GET':
        form = PortadorForm(request.POST or None)
        return render(request, 'create_portador.html', {
            'form': form
        })
    else:
        form = PortadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('portadores')
 
@login_required    
def editar_portador(request, id):
    portador =   get_object_or_404(Portador,CUIP=id)
    form = PortadorForm(request.POST or None, request.FILES or None, instance=portador)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('portadores')
    return render(request, 'edit_portador.html', {
    'form': form
    })

@login_required
def eliminar_portador(request, id):
    try:
     portador = Portador.objects.get(CUIP=id) 
     portador.delete()
    except Exception as e: 
        messages.error(request, f"error: {e}")
    return redirect('portadores')
          