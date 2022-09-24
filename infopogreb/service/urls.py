from django.urls import path
from . import views


urlpatterns = [
    path('service/', views.service, name='service'),
    path('detail_service/<str:slug>', views.detail_service, name='detail_service'),
    
]