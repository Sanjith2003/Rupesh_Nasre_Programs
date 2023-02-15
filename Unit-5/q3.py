from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def shop(request):
    items = Item.objects.all()

    # Apply category filter if provided in GET parameters
    if 'category' in request.GET:
        category = request.GET['category']
        items = items.filter(category=category)

    # Apply price filter if provided in GET parameters
    if 'price' in request.GET:
        price = request.GET['price']
        if price == 'asc':
            items = items.order_by('price')
        elif price == 'desc':
            items = items.order_by('-price')

    context = {'items': items}
    return render(request, 'shop.html', context)
