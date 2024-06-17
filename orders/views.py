from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from shop.models import Product
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item["product"],
                                         price=item['price'], quantity=item['quantity'])
                product = get_object_or_404(Product, id=item['product_id'])
                if product.quantity == item['quantity']:
                    product.quantity = 0
                    product.available = False
                else:
                    product.quantity -= item['quantity']
                product.save()
            cart.clear()

            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
