from django.views.generic import View
from django.shortcuts import render, redirect

class Dash(View):
    def get(self, request):
      if (request.user.is_staff == True):
        return render(request, 'dashboard.html')
      else:
        return render(request, 'not_eligible.html')