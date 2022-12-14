from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import CategoryService, Service, Coment
from .forms import ServiceForm, ComentForm
from django.core.paginator import Paginator
from django.db.models import Count
from django.views.generic import ListView, DetailView, CreateView



def service(request):
    cats = CategoryService.objects.annotate(Count ('service'))
    services = Service.objects.order_by('-created')
    contact_list = Service.objects.order_by('-created')
    paginator = Paginator(contact_list, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'service/service.html', {'page_obj': page_obj, 'cats': cats, 'services': services})


# class DetailService(DetailView):
#     template_name = 'service/detail_service.html'
#     model = Service
#     context_object_name = 'detail'
    
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.views += 1
#         self.object.save()
#         context = self.get_context_data(object=self.object)
#         return self.render_to_response(context)


def detail_service(request, slug):
    detail = get_object_or_404(Service,slug=slug)
    #coment = Coment.objects.filter(serv=pk, moderation=True)
    coment = detail.coment_service.filter(moderation=True)
    if request.method == "POST":
        form = ComentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.serv = detail
            form.detail = detail
            form.save()
            return redirect(detail_service, slug)
    else:
        form = ComentForm()
    return render(request, 'service/detail_service.html',{'detail': detail, 'coments': coment, 'form': form})


def get_category_service(request, category_id):
    cats = CategoryService.objects.annotate(Count ('service'))
    services = Service.objects.filter(category_id=category_id).order_by('-created')
    categorys = CategoryService.objects.all()
    category = CategoryService.objects.get(pk=category_id)
    contact_list = Service.objects.order_by('-created')
    paginator = Paginator(contact_list, 8) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'service/category_service.html', {'services': services, 'categorys': categorys, 'category': category, 'page_obj':page_obj, 'contact_list': contact_list, 'cats': cats})


def service_new(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('service')
    else:
        form = ServiceForm()
    
    return render(request, 'service/service_new.html', {'form': form})


def service_edit(request, slug):
    post = Service.objects.get(slug__iexact=slug)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('detail_service', slug=post.slug)
    else:
        form = ServiceForm(instance=post)
    return render(request, 'service/service_update.html', {'form': form, 'post':post})


def service_delete(request, slug):
    post = get_object_or_404(Service, slug__iexact = slug)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('service'))
    else:
        post = get_object_or_404(Service, slug__iexact = slug)
    return render(request, 'service/service_delete.html', {'post': post})