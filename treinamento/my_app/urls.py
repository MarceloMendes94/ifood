from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    #path('index/<str:name>',views.home ,name='home'),
    path('person/',views.person, name='person'),
    path('lanchonete/', views.listar_lanchonetes, name = 'listar lanchonetes' ),
    path('lanchonete/<str:nome>/', views.buscar_lanchonete, name = 'buscar lanchonete'),
]
