from django.shortcuts import render

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.views.decorators.http import require_POST
from django.utils import timezone

from cart.utils.cart import Cart
from orders.forms import CouponForm, OrderCreateForm
from orders.models import Order, OrderItem


@login_required(login_url='/accounts/login/?next=/orders/create/')
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, 'Вітаю з покупкою')
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order.html',
                          {'order': order, 'form': form})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order.html',
                  {'cart': cart, 'form': form})


@login_required()
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = CouponForm()
    return render(request, 'orders/order.html', {'order': order, 'form': form})



