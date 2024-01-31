#from django.shortcuts import render

from django.http import HttpResponse

def food(request):
    msg="butter chicken"

    return HttpResponse(msg)

# Create your views here.
