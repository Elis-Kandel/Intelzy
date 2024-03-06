from django.shortcuts import HttpResponse,render
from django.http import JsonResponse
def hello_view(request):
    test={'name':'elis'}
    print(type(test))
    return JsonResponse(test)
def func(request):
    return render(request,"index.html")