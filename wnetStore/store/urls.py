from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

# Config para archivos estaticos, por ejem. imagenes y logos.
# urlpatterns = staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
	#Leave as empty string for base url
    url(r'^admin/', admin.site.urls),
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('products/', views.ProductList.as_view(), name="products"),
	url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
	
]