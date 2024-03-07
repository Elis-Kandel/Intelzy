from django.shortcuts import HttpResponse,render
from django.http import JsonResponse
todos=[{'{name':'elis',
        'id':1},
          {'name':'Paat',
           'id':2}]
def todo(request):
    print(type(todos))
    return JsonResponse(todos, safe=False)
def read_todo(request, todoId):
    print("TodoId",todoId)
    todo=None
    for i in todos:
        if i["id"] is todoId:
            todo=i
            break
    print(todo)
    return JsonResponse(todo, safe=False)
