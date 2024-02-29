from django.shortcuts import render
from django.http import JsonResponse
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    data = {'orders': list(orders.values())}
    return JsonResponse(data)
