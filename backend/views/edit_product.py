from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from product.models import Product as ProductTable

class EditProduct(View):
    def get(self, request):
        if (request.user.is_staff == True):
            productlist = ProductTable.objects.all()
            return render(request, 'edit_product.html', {'productlist': productlist})
        else:
            return render(request, 'not_eligible.html')

    def post(self, request):
        return JsonResponse("sdfsdfsgss")