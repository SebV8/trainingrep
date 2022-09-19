from multiprocessing import context
from django.shortcuts import render, redirect
from entrenamiento.models import *
from entrenamiento.forms import *

def training(request):
    prs = Pr_detail.objects.all()
    rms = Rm_detail.objects.all()
    tc = TimeCap_detail.objects.all()
    context = {'prs': prs, 'rms': rms, 'tc': tc}
    return render(request, 'training.html', context)

def create_pr(request):
    form = Pr_detailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('training')
    return render(request, 'create_pr.html', {'form': form})

def update_pr(request, id):
    prs = Pr_detail.objects.get(id=id)
    if request.method == 'POST':
        form = Pr_detailForm(request.POST, request.FILES, instance=prs)
        if form.is_valid():
            form.save()
            return redirect('training')
    else:
        form = Pr_detailForm(instance=prs)
    context = {'form': form}
    return render(request, 'update_pr.html', context)

def delete_pr(request, id):
    prs = Pr_detail.objects.get(id=id)
    prs.delete()
    return redirect('training')



def create_rm(request):
    form = Rm_detailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('training')
    return render(request, 'create_pr.html', {'form': form})

def update_rm(request, id):
    rms = Rm_detail.objects.get(id=id)
    if request.method == 'POST':
        form = Rm_detailForm(request.POST, request.FILES, instance=rms)
        if form.is_valid():
            form.save()
            return redirect('training')
    else:
        form = Rm_detailForm(instance=rms)
    context = {'form': form}
    return render(request, 'update_pr.html', context)

def delete_rm(request, id):
    rms = Rm_detail.objects.get(id=id)
    rms.delete()
    return redirect('training')
