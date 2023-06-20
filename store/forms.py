from django import forms
from listelement.models import Category, Type

class ProductForm(forms.Form):
    title = forms.CharField(label="Titulo", max_length=255, min_length=8, required=True)
    description = forms.CharField(label="Descripcion",required=True, widget=forms.Textarea)
    price = forms.DecimalField(label="Precio", min_value=0.01)
    category = forms.ModelChoiceField(label="Categoria", queryset=Category.objects.all())
    type = forms.ModelChoiceField(label="Tipo", queryset=Type.objects.all())
