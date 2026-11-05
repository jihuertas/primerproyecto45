
from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal,name='principal'),
    path('ji',views.ji,name='ji'),
    path('alumnado/javier',views.alumnado,name='javier'),
    path('<int:pk>',views.detalle_post, name='detalle'),
    path('autores',views.autores, name='autores'),
    path('autor/<int:pk>',views.autor, name='autor'),

    path('categoria/<int:pk>',views.categoria, name='categoria'),
]
