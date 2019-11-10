from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse

class ProductDetails(View):
    def get(self, request):
        # return render(request, 'productup.html')
        return HttpResponse("hello")

    def post(self, request):
        return JsonResponse("sdfsdfsgss")
