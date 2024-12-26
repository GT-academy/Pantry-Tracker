from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('agregar/', views.agregar_articulo, name='agregar_articulo'),
    path('usar/<int:id>/', views.marcar_usado, name='marcar_usado'),
    path('eliminar/<int:id>/', views.eliminar_articulo, name='eliminar_articulo'),
    path('editar/<int:id>/', views.editar_articulo, name='editar_articulo'),
    path('exportar/', views.exportar_csv, name='exportar_csv'),
    path('historial/', views.historial_usados, name='historial_usados'),
]
