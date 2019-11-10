from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

class Location(View):
    def get(self, request):
            return render(request, 'location.html')

    def post(self, request):
        return JsonResponse("dfvfdvbbfddfb")