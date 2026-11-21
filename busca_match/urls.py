from django.urls import path
from . import views

urlpatterns = [
    path('', views.busca_carona, name='busca_carona'),
    path('confirmar/<int:carona_id>/', views.confirmar_match, name='confirmar_match'),
]