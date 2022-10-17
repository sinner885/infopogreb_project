from django.urls import path
from . import views


urlpatterns = [
    path('adv/', views.adv, name='adv'),
    path('adv_new/', views.adv_new, name='adv_new'),
    path('detail_adv/<int:pk>', views.detail_adv, name='detail_adv'),
    path('detail_adv/<int:pk>/delete/', views.adv_delete, name='adv_delete'),
    
]