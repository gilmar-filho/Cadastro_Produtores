'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pessoas, name='listar_pessoas'),
    path('cadastrar/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('editar/<int:pk>/', views.editar_pessoa, name='editar_pessoa'),
    path('deletar/<int:pk>/', views.deletar_pessoa, name='deletar_pessoa'),
]
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('lista/', views.listar_pessoas, name='listar_pessoas'),
    path('editar/<int:pk>/', views.cadastrar_pessoa, name='editar_pessoa'),
    path('deletar/<int:pk>/', views.deletar_pessoa, name='deletar_pessoa'),
    path('buscar/', views.buscar_pessoas, name='buscar_pessoas'),
    path('exportar/', views.exportar_pdf_todos, name='exportar_pdf_todos'),
    path('exportar_periodo/', views.exportar_por_periodo, name='exportar_por_periodo'),
]
