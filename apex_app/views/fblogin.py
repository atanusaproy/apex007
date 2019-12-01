from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from ..models import User_details
import json


class FBLogin(View):
    def get(self):
        pass

    def post(self, request):
        try:
            fbdetails = request.POST.get('fbdetails')
            details = User_details()
            details.user_id = 0
            details.fb_details = json.dumps(fbdetails)
            details.save()
            return JsonResponse({'type': 'success', 'data': 'Successfully received'})
            # if details.save():
            #     return JsonResponse({'type': 'success', 'data': 'Successfully received'})
            # else:
            #     return JsonResponse({'type': 'error', 'data': 'Login failed'})
        except Exception as e:
            return JsonResponse({'type': 'error', 'message': str(e)})

