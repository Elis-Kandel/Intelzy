from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import User


def index(request):
    table=User.objects.all()
    return HttpResponse(table)
def delete(request,updateId):
    table=User.objects.get(id=updateId)
    table.delete()
    return HttpResponse("You have deleted {updateId}")
def update(request,updateId):
    table=User.objects.get(id=updateId)
    table.gender=1
    table.save()
    return HttpResponse("You have updated")
def list(request):
    db_user = User.objects.all()
    response =[]
    for i in db_user:
        response.append({"username":i.username,"email":i.email,"gender":i.gender})
    return JsonResponse(response,safe=False)
def read(read,updateId):
    table=User.objects.get(id=updateId)
    print(table)
    return JsonResponse({
        "username":table.username
        
        },safe=False)
