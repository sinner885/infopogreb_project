from django.urls import path
from . import views
from .feeds import LatestAdvertFeed

urlpatterns = [
    path('', views.home, name='home'),
    path('advert/', views.advert, name='advert'),
    path('detail_advert/<str:slug>', views.detail_advert, name='detail_advert'),
    path('advert_new/', views.advert_new, name='advert_new'),
    path('detail_advert/<str:slug>/update/', views.advert_edit, name='advert_edit'),
    path('detail_advert/<str:slug>/delete/', views.advert_delete, name='advert_delete'),
    path('category/<int:category_id>',views.get_category, name='category'),
    path('feed/', LatestAdvertFeed(), name='advert_feed'),
    
]