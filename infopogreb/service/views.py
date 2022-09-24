from django.shortcuts import render, get_object_or_404
from .models import CategoryService, Service
from django.core.paginator import Paginator
from django.db.models import Count

def service(request):
    cats = CategoryService.objects.annotate(Count ('service'))
    services = Service.objects.order_by('-created')
    contact_list = Service.objects.order_by('-created')
    paginator = Paginator(contact_list, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'service/service.html', {'page_obj': page_obj, 'cats': cats, 'services': services})



def detail_service(request, slug):
    detail = get_object_or_404(Service, slug__iexact = slug)
    return render(request, 'service/detail_service.html',{'detail': detail})