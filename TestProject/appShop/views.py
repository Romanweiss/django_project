from itertools import product
from tkinter import NO
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import ProductShop


class HomePage(View):
    def get(self, request):
        obj_products = ProductShop.objects.values("id", "title", "count", "price")
        return render(request, "appShop/home.html", {"product": obj_products})

    def post(self, request):
        product_id = request.POST["id"]
        key_bucket = request.session.get("bucket")
        if key_bucket == None:
            request.session["bucket"] = [product_id]
        else:
            # data = list(request.session['bucket'])
            # print(request.session)
            request.session['backed'] = list(key_bucket) + [product_id]
        
        print(request.session['backed'])
        return JsonResponse({})
