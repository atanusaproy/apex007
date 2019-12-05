from django.views.generic import View
from django.shortcuts import render, redirect

class Dash(View):
    def get(self, request):
        return render(request, 'dashboard.html')
