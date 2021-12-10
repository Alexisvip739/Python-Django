from django.http import HttpResponse
from datetime import datetime
def Hola_Mundo(request):
    now=datetime.now().strftime('%b %dth, %Y ')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))

def hi(request):
    return HttpResponse('Hi!')