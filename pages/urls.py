from django.urls import path 
from .views import homePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView

from . import views


urlpatterns = [ 

    path('', homePageView.as_view(), name='home'),
    path('crear/', views.FormularioCreacion.as_view(), name='formulario_creacion'),
    path('listar/', views.ListarPedidos.as_view(), name='listar_pedidos'),
    path('ver/<int:pk>/', views.VerPedido.as_view(), name='ver_pedido'),
    path('eliminar/<int:pedido_id>/', views.EliminarPedido.as_view(), name='eliminar_pedido'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

] 

