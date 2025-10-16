from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_casa, name='ver_casa'),
    path('agregar/', views.agregar_casa, name='agregar_casa'),
    path('editar/<int:id>/', views.editar_casa, name='editar_casa'),
    path('borrar/<int:id>/', views.borrar_casa, name='borrar_casa'),
]