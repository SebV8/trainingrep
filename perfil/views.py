from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Perfil
from .forms import PerfilForm

# Create your views here.
def index(request):
    profile = Perfil.objects.get(id=1)
    context = {'profile': profile}
    return render(request, 'perfil.html', context)

def create(request):
    form = PerfilForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PerfilForm()
        return redirect('index')
    context = {'form': form}
    return render(request, 'create.html', context)

def update(request, id):
    profile = Perfil.objects.get(id=id)
    # image = request.FILES.get('image')
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PerfilForm(instance=profile)
    context = {'form': form}
    return render(request, 'edit.html', context)

def delete(request, id):
    profile = Perfil.objects.get(id=id)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')
    context = {'profile': profile}
    return render(request, 'delete.html', context)