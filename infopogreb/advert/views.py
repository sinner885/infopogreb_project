import re
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.db.models import Count

from django.contrib.auth import login, logout
from django.core.paginator import Paginator

from .models import *
from .forms import *


def home(request):
    categorys = Category.objects.all()
    cats = Category.objects.annotate(Count ('advert'))
    adverts = Advert.objects.order_by('-created')[:5]
    return render(request, 'advert/home.html', {'categorys': categorys, 'adverts': adverts, 'cats': cats}) 




def advert(request):
    #categorys = Category.objects.all()
    cats = Category.objects.annotate(Count ('advert'))
    adverts = Advert.objects.order_by('-created')
    contact_list = Advert.objects.order_by('-created')
    paginator = Paginator(contact_list, 8) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'advert/advert.html', {'page_obj': page_obj, 'cats': cats, 'adverts': adverts})


def detail_advert(request, slug):
    detail = get_object_or_404(Advert, slug__iexact = slug)
    
    return render(request, 'advert/detail_advert.html',{'detail': detail})


def get_category(request, category_id):
    adverts = Advert.objects.filter(category_id=category_id)
    categorys = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    contact_list = Advert.objects.order_by('-created')
    paginator = Paginator(contact_list, 8) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'advert/category.html', {'adverts': adverts, 'categorys': categorys, 'category': category, 'page_obj':page_obj, 'contact_list': contact_list})


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви зареєстровані')
            return redirect('login')
        else:
            messages.error(request, "Помилка реєстрації")
    else:
        form = RegisterUserForm()
    return render(request, 'register.html',{'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def advert_new(request):
    if request.method == 'POST':
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('advert')
    else:
        form = AdvertForm()
    
    return render(request, 'advert/advert_new.html', {'form': form})


def advert_edit(request, slug):
    post = Advert.objects.get(slug__iexact=slug)
    if request.method == 'POST':
        form = AdvertForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('detail_advert', slug=post.slug)
    else:
        form = AdvertForm(instance=post)
    return render(request, 'advert/advert_update.html', {'form': form, 'post':post})


def advert_delete(request, slug):
    post = get_object_or_404(Advert, slug__iexact = slug)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('advert'))
    else:
        post = get_object_or_404(Advert, slug__iexact = slug)
    return render(request, 'advert/advert_delete.html', {'post': post})