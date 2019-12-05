from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from product.models import Product as ProductTable

class Manage(View):
    def get(self, request):
        productlist = ProductTable.objects.all()
        return render(request, 'manage_index.html', {'productlist' : productlist})

    def post(self, request):
        return JsonResponse("sdfsdfsgss")
