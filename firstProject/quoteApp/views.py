from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def quoteMe(request):
    return HttpResponse("<h2>The best investment is investing in yourself</h2>")
