from django.shortcuts import render
from .models import Tag, Product

def product_list_view(request):
    tag_name = request.GET.get('tag')
    if tag_name:
        products = Product.objects.filter(tags__name=tag_name)
    else:
        products = Product.objects.all()
    tags = Tag.objects.all()
    return render(request, 'gadjets/product_list.html', {
        'products': products,
        'tags': tags
    })

