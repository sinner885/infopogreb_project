from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('advert/', views.advert, name='advert'),
    path('detail_advert/<str:slug>', views.detail_advert, name='detail_advert'),
    path('advert_new/', views.advert_new, name='advert_new'),
    path('category/<int:category_id>',views.get_category),
    
]