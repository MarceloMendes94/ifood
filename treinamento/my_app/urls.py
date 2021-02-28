from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    #path('index/<str:name>',views.home ,name='home')
    path('lanchonete/', views.listar_lanchonetes, name = 'listar lanchonetes' ),
    path('lanchonete/<str:nome>/', views.buscar_lanchonete, name = 'buscar lanchonete'),
    path('estado/<str:sigla>/', views.buscar_estado, name = 'buscar por estado'),
    path('estado/<str:sigla>/cidade/<str:cidade>/', views.buscar_estado_cidade, name = 'buscar por estado cidade'),    
    path('estado/<str:sigla>/cidade/<str:cidade>/max-preco/<int:valor>/', views.buscar_estado_cidade_max_preco, name = 'buscar por estado, cidade e valor maximo'),
    path('max-preco/<int:valor>/', views.buscar_max_preco, name = 'buscar por preco maximo'),

    


]
