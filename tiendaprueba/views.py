from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Product
# Create your views here.

def hello_world(request):
	product = Product.objects.order_by('id')
	template = loader.get_template('index.html')
	context = { #Diccionario que se le pasa al HTML
		'product': product
	}
	return HttpResponse(template.render(context, request))
