from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['Товар'],
                    price=item['Ціна'],
                    quantity=item['Кількість']
                )
            cart.clear()
            return render(request, template_name='orders/order/created.html', context={'order': order})
    else:
        form = OrderCreateForm()
    return render(request, template_name='orders/order/create.html', 
                    context={
                        'form': form,
                        'cart': cart
                    }
            )