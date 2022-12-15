from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from store.models import Cart, Order, Product


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'products': products})


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/details.html', context={'product': product})


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, "store/cart.html", context={"items": cart.orders.all()})


def cart_add(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(product=product, ordered=False, user=user)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse('product', kwargs={'slug': slug}))


def cart_delete(request):
    if cart := request.user.cart:
        cart.delete()

    return redirect("index")
