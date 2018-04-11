from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
	path('', views.hello_world, name='hello'), #En la raiz de la app se muestra lo que está despues de la coma
	#re_path(r'^product/(?P<pk>[0-9]+)/$', views.product_detail),
	path('product/new', views.new_product, name="new_product"),
	path('product/<pk>', views.product_detail),

]