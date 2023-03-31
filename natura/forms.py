from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=250)

class BuscarProductoForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)


class ConsultoraForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    codigoCN = forms.CharField(max_length=7)
    zona = forms.CharField(max_length=100)

class BuscarConsultoraForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=20)
    pedido = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    consultora = forms.CharField(max_length=200)

class BuscarClienteForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)