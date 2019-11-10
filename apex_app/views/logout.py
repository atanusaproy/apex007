from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import logout


class Logout(View):
     def get(self, request):
         try:
             logout(request)
             # return JsonResponse({'type': 'success', 'data': 'Successfully Logged out'})
             return redirect("home")
         except:
             return JsonResponse({'type': 'error', 'message': 'Problem in our server please try again'})

     def post(self, request):
         try:
             logout(request)
             # return JsonResponse({'type': 'success', 'data': 'Successfully Logged out'})
             return redirect("home")
         except:
             return JsonResponse({'type': 'error', 'message': 'Problem in our server please try again'})