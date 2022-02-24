from django.http import HttpResponse
from django.shortcuts import render
from crypto.models import CryptoCurrency

menu = [i for i in CryptoCurrency.objects.values('title').order_by("time_create").last()]

def index(request):
    return render(request, 'crypto/index.html', {'menu': menu})
