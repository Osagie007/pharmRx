from django.urls import path
from . import views

#app_name = 'pharmRx'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('product_info/<int:product_id>', views.product_info, name='product_info'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    #path('customer_info', views.customer_info, name='customer_info'),
]