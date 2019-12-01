from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from ..models import Product as ProductTable
from datetime import datetime
import time

class ProductUpload(View):
    def get(self, request):
        if(request.user.is_staff == True):
            return render(request, 'product.html')
        else:
            return render(request, 'not_eligible.html')

    def post(self, request):
        file_name = ""
        pname = request.POST['pname']
        ptype = request.POST['ptype']
        pdesc = request.POST['desc']
        pavil = request.POST['avail']

        fileimg = request.FILES['xfile']
        name_split = fileimg.name.split('.')
        # filenamelist = ["8-1024x768", "jpg"]
        extension = name_split[len(name_split) - 1]
        fls = FileSystemStorage()
        filename = str(time.time())+"."+extension
        ff = fls.save("UploadedFiles/" + filename, fileimg)

        product_table = ProductTable()
        product_table.name = pname
        product_table.type = ptype
        product_table.image = filename
        product_table.description = pdesc
        # product_table.availability = pavil
        product_table.save()

        # file_name = file_name + "<br>" + str(i) + ") File Name :- " + fls.url(ff)

        # i = 0
        # for file in request.FILES:
        #     i = i + 1
        #     fileimg = request.FILES[file]
        #     fls = FileSystemStorage()
        #     ff = fls.save("UploadedFiles/" + fileimg.name, fileimg)
        #     file_name = file_name + "<br>" + str(i) + ") File Name :- " + fls.url(ff)



        # return JsonResponse({'type': 'success', 'data': pname})
        return render(request, 'product.html')