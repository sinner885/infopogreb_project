from django.urls import path
from . import views


urlpatterns = [
    path('service/', views.service, name='service'),
    path('detail_service/<str:slug>', views.detail_service, name='detail_service'),
    path('service_new/', views.service_new, name='service_new'),
    path('detail_service/<str:slug>/update/', views.service_edit, name='service_edit'),
    path('detail_service/<str:slug>/delete/', views.service_delete, name='service_delete'),
    path('category/<int:category_id>', views.get_category_service, name='category_service'),
    
]