from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def check(request):
    return JsonResponse("You have paid",safe=False)