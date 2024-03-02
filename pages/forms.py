from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha', 'direccion', 'cantidad']  # Excluir 'precio' de los campos del formulario
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        if cantidad is not None:
            precio = cantidad * 10
            cleaned_data['precio'] = precio
        return cleaned_data
