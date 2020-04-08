from django.shortcuts import render, redirect, reverse, get_object_or_404


# Create your views here.
from blog.models import Post
from store.models import Store


def view_cart(request):
    posts = Post.objects.all()
    return render(request, "cart/cart.html", {"posts": posts})


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


def cart_remove(request, store_id):
    cart = view_cart(request)
    store = get_object_or_404(Store, id=store_id)
    cart.remove(store)
    return redirect(reverse('view_cart'))
