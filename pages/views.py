from django.shortcuts import render, redirect
from django import forms 
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse


from django.views.generic import ListView

from django.views.generic import DetailView

from django.urls import reverse_lazy

from .models import Pedido
from .forms import PedidoForm


from django.contrib import messages
# Create your views here.

# def homePageView(request):
#     return HttpResponse('Hello World!')

class homePageView(TemplateView):
    template_name = 'home.html'
    
class VistaInicial(View):
    def get(self, request):
        return render(request, 'pedido/vista_inicial.html')





class FormularioCreacion(View):
    def get(self, request):
        form = PedidoForm()
        return render(request, 'pedido/formulario_creacion.html', {'form': form})
    
    def post(self, request):
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Elemento creado satisfactoriamente.')
            return redirect('listar_pedidos')  # Redirigir a la lista de pedidos
        return render(request, 'pedido/formulario_creacion.html', {'form': form})

class ListarPedidos(View):
    def get(self, request):
        pedidos = Pedido.objects.all()
        return render(request, 'pedido/listar_pedidos.html', {'pedidos': pedidos})
    
class VerPedido(DetailView):
    model = Pedido
    template_name = 'pedido/ver_pedido.html'
    context_object_name = 'pedido'


class EliminarPedido(View):
    def post(self, request, pedido_id):
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.delete()
        messages.success(request, 'Pedido eliminado exitosamente.')
        return redirect('listar_pedidos')

class BorrarPedido(View):
    def get(self, request, id_pedido):
        pedido = Pedido.objects.get(id=id_pedido)
        pedido.delete()
        return redirect('listar_pedidos')

class MensajeCreacionExitosa(View):
    def get(self, request):
        return render(request, 'pedido/mensaje_creacion_exitosa.html')

    
class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            
            "title": "Roods - Online Store", 
            "subtitle": "About us", 
            "description": "We are the best store in the world!", 
            "author": "Developed by: Juanmi Castro", 
        }) 
        return context 
    


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = 'rood69@latinxs.com'
        context['address'] = '666 Eafit, Medellin'
        context['phone'] = '+51 321 746 9837'
        return context


class Product: 
    products = [ 
        {"id":"1", "name":"Guitar", "description":"Great IOT Guitar", "price":4}, 
        {"id":"2", "name":"Bike", "description":"Great IOT Bike", "price":2}, 
        {"id":"3", "name":"Chair", "description":"Great IOT Chair", "price":3}, 
        {"id":"4", "name":"Pencil", "description":"Great IOT Pencil", "price":8} 
    ] 


class ProductIndexView(View): 
    template_name = 'pages/products/index.html' 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
        return render(request, self.template_name, viewData) 

class ProductShowView(View):
    template_name = 'pages/products/show.html'

    def get(self, request, id):
        viewData = {}

        try:
            product = Product.products[int(id) - 1]

            viewData["title"] = product["name"] + " - Online Store"

            viewData["subtitle"] = product["name"] + " - Product information"

            viewData["product"] = product

            return render(request, self.template_name, viewData)
        except IndexError:
            return HttpResponseRedirect(reverse('home'))

    
    
class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True)
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and  price < 0:
            raise forms.ValidationError("Price must be greater than zero")
        return price



class ProductCreateView(View): 
    template_name = 'pages/products/create.html' 
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
    
    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            return render(request, 'pages/products/product_created.html')
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)