from django.shortcuts import render, redirect, get_object_or_404
from .models import Adv
from .forms import AdvForm, AdvComentForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse

def adv(request):
    advs = Adv.objects.order_by('-created')
    contact_list = Adv.objects.order_by('-created')
    paginator = Paginator(contact_list, 8) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'adv/adv.html', {'page_obj': page_obj, 'advs': advs})


def adv_new(request):
    if request.method == 'POST':
        form = AdvForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = AdvForm()
    
    return render(request, 'adv/adv_new.html', {'form': form})


def detail_adv(request, pk):
    detail = get_object_or_404(Adv, pk = pk)
    coment = detail.coment_adv.filter(moderation=True)
    if request.method == "POST":
        form = AdvComentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.adv = detail
            form.detail = detail
            form.save()
            return redirect(detail_adv, pk)
    else:
        form = AdvComentForm()
    return render(request, 'adv/detail_adv.html', {'detail': detail, 'coments': coment, 'form': form})


def adv_delete(request, pk):
    post = get_object_or_404(Adv, pk = pk)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('adv'))
    else:
        post = get_object_or_404(Adv, pk = pk)
    return render(request, 'adv/adv_delete.html', {'post': post})