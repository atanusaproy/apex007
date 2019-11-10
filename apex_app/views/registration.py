from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from ..models import User_details

class Regis(View):
    def get(self, request):
        return render(request, "registration.html")

    def post(self, request):
        try:

            user = User.objects.create_user(username=request.POST.get('username'),
                                          password=request.POST.get('pass'),
                                           email=request.POST.get('email'))
            user.save()
            user.first_name = request.POST.get('username')
            user.save()
            detail = User_details.objects.create(phone=request.POST.get('phone'),user_id=user.id)
            detail.save()

            arr = {'type': 'success', 'data': "saved"}

            return JsonResponse(arr)




        except Exception as e:

            arr = {'type': 'error', 'message': str(e)}

            return JsonResponse(arr)
