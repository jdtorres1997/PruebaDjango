#aqui se almacenan los formularios, credos a partir de los modelos

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'