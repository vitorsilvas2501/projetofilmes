from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('cadastro/', views.cadastro, name='cadastro'),
path('lista/', views.lista, name='lista'),
path('detalhes/<int:filme_id>/', views.detalhes, name='detalhes'),
path('deletar/<int:filme_id>/', views.deletar, name='deletar'),
path('atualizar/<int:filme_id>/', views.atualizar, name='atualizar')
]
