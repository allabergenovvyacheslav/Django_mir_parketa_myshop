from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


# представление обработки формы и создания нового заказа
def order_create(request):
    """
    В представлении order_create текущая корзина извлекается из сеанса посредством инструкции cart = Cart(request).
    В зависимости от метода запроса выполняется следующая работа:
    •• запрос методом GET: создает экземпляр формы OrderCreateForm и прорисовывает шаблон orders/order/create.html;
    •• запрос методом POST: выполняет валидацию отправленных в запросе данных. Если данные валидны, то в базе данных создается новый заказ,
    используя инструкцию order = form.save(). Товарные позиции корзины прокручиваются в цикле, и для каждой из них создается OrderItem.
    Наконец, содержимое корзины очищается, и шаблон orders/order/created.html прорисовывается.
    :param request:
    :return:
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid:
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # очистить корзину
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
