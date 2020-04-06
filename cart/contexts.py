from django.shortcuts import get_object_or_404
from store.models import Store


def cart_contents(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    store_count = 0

    for id, quantity in cart.items():
        store = get_object_or_404(Store, pk=id)
        # remove = request.session.pop('cart', {id})
        total += quantity * store.price
        store_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'store': store})

    return {'cart_items': cart_items, 'total': total, 'store_count': store_count}

#
# def remove(self, store):
#
#     store_id = str(store.id)
#     if store_id in self.cart:
#         self.cart[store_id]['quantity'] -= 1
#         if self.cart[store_id]['quantity'] == 0:
#             del self.cart[store_id]
#         self.save()