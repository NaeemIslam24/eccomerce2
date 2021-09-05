from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import *

# Create your views here.
def shop(request):
    template = 'shop.html'
    products = Product.objects.all()

    paginator = Paginator(products, 3)

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context= {

        'products': post,
        
        'page_ob': page,
        
    }

    return render(request, template_name = template, context = context)


def product_details(request):
    template = 'product-details.html'
    context= {
        
    }

    return render(request, template_name = template, context = context)

def checkout(request):
    template = 'checkout.html'
    if request.user.is_authenticated:
        customer = request.user.customer #user app to customer app with one to one relation
        order = Order.objects.get(customer = customer, complete=False)
        items = order.orderitem_set.all()  # it will return exact user's order item
            # items = OrderItem.objects.all() # it will return all user's order item
    else:
        items = []

    context= {
        'orderItems': items,
        'order':order,
    }

    return render(request, template_name = template, context = context)

def cart(request):
    template = 'cart.html'
    if request.user.is_authenticated:
        customer = request.user.customer #user app to customer app with one to one relation
        order = Order.objects.get(customer = customer, complete=False)
        items = order.orderitem_set.all()  # it will return exact user's order item
            # items = OrderItem.objects.all() # it will return all user's order item
    else:
        items = []

    context= {
        'orderItems': items,
        'order':order,
    }

    return render(request, template_name = template, context = context)