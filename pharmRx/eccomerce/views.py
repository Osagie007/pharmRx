from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
from django.core.paginator import Paginator
from .utils import cookieCart, cartData, guestOrder
import json
import datetime
from django.http import JsonResponse
from .forms import Paystack_CustomerInfoForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    products = Product.objects.all()
    carousel_products = products[:4]
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'products': products, "carousel_products": carousel_products, 'cartItems': cartItems}
    return render(request, 'eccomerce/index.html', context)


def store(request):
    products = list(Product.objects.all())
    paginator = Paginator(products, per_page=6)
    page = request.GET.get('page')
    p_products = paginator.get_page(page)
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'products': products, 'p_products': p_products, 'cartItems': cartItems}
    return render(request, 'eccomerce/shop.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'eccomerce/cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']

    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'eccomerce/checkout.html', context)
    
    

def about(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'eccomerce/about.html', context)


def product_info(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    data = cartData(request)
    cartItems = data['cartItems']

    context = {'product': product, 'cartItems': cartItems}
    return render(request, 'eccomerce/shop-single.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)   
    orderItem.save()

    if action == 'remove-all':
        orderItem.delete() 

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
         customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()
    
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            country=data['shipping']['country']
        )
    
    return JsonResponse('Payment Complete', safe=False)

# Paystack option will be added in upgrade

# def customer_info(request):
#     if request.method == 'POST':
#         customer_form = Paystack_CustomerInfoForm(request.method)
#         if customer_form.is_valid()and customer_form.cleaned_data:
#             customer_form.save()
#             return render(request, 'eccomerce/payment.html',
#                           {'email':customer_form.email})
#         else:
#             return HttpResponse('Invalid input try again!!!')
#     else:
#         customer_form = Paystack_CustomerInfoForm()
#     return render(request, 'eccomerce/customer_info.html',
#                     {'customer_form': customer_form})


def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    if request.method == 'POST':
        res = request.POST
        print(res)
        contact_data = request.POST
        Contact.objects.create(
         first_name = contact_data['c_fname'],
         last_name = contact_data['c_lname'],
         email = contact_data['c_email'],
         subject = contact_data['c_subject'],
         message = contact_data['c_message']
        )
        messages.success(request, 'Message sent')
        return redirect('contact') 
    else:
        return render(request, 'eccomerce/contact.html', context)
       


# FOR NAME 

# @csrf_exempt
# def search(request):
#     products = Product.objects.all()
#     print(products)
#     p_name = []
#     for product in products:
#         p_name.append(product.name)
#     print(p_name)
#     if request.method == 'POST':
#         #query = request.POST.get('c_search', '')
#         query = request.POST
#         print(query)
#         query_data = query['c_search']
#         print(query_data)
#         result = []
#         for p in p_name:
#             if query_data.lower() in p.lower():
#                 result.append(p)
#         print(result)
        
        
#         context = {'res': result, 'query_data': query_data}
#         return render(request, 'eccomerce/search_results.html', context)

#     return redirect('home')

@csrf_exempt
def search(request):
    products = Product.objects.all()
    print(products)

    data = cartData(request)
    cartItems = data['cartItems']

    p_dict = []
    for product in products:
        print(product.id)
        p_dict.append({'id':product.id,
                       'name':product.name
                       })
        
    print(p_dict)
    if request.method == 'POST':
        query = request.POST
        print(query)
        query_data = query['c_search']
        print(query_data)
        result = []
        for p in p_dict:
            if query_data.lower() in p['name'].lower():
                result.append(p)
        print(result)
        
        context = {'res': result, 'query_data': query_data, 'cartItems': cartItems}
        return render(request, 'eccomerce/search_results.html', context)

    return redirect('home')
    