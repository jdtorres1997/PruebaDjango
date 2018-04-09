#from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
	path('', views.hello_world, name='hello'), #En la raiz de la app se muestra lo que está despues de la coma
]