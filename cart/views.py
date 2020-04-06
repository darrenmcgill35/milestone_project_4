from django.shortcuts import render, redirect, reverse, get_object_or_404


# Create your views here.
from store.models import Store


def view_cart(request):
    return render(request, "cart/cart.html")


def add_to_cart(request, store_id):

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if store_id in cart:
        cart[store_id] = int(cart[store_id]) + quantity
    else:
        cart[store_id] = cart.get(store_id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('store'))


def adjust_cart(request, store_id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[store_id] = quantity
    else:
        cart.pop(store_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

