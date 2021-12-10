
from django.views import View
from .models import  Company
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.

class CompanyListView(View):
    def get(self,request):
        Cllist = Company.objects.all()
        return JsonResponse(list(Cllist.values()),safe=False)## false es para que regrese el arreglo y no el json

    




class CompanyDetailsView(View):
    def get(self,request,pk):
        company = Company.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company))
  

