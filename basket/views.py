from django.shortcuts import render, redirect, get_object_or_404
from .models import basketmodel
from .forms import BasketForm

# Список заказов
def basket_list(request):
    baskets = basketmodel.objects.all()
    return render(request, 'basket_list.html', {'baskets': baskets})

# Создать заказ
def basket_create(request):
    if request.method == 'POST':
        form = BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm()
    return render(request, 'basket_form.html', {'form': form})

# Изменить заказ
def basket_update(request, pk):
    basket = get_object_or_404(basketmodel, pk=pk)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm(instance=basket)
    return render(request, 'basket_form.html', {'form': form})

# Удалить заказ
def basket_delete(request, pk):
    basket = get_object_or_404(basketmodel, pk=pk)
    if request.method == 'POST':
        basket.delete()
        return redirect('basket_list')
    return render(request, 'basket_confirm_delete.html', {'basket': basket})

