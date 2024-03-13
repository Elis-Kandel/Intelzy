from django.shortcuts import HttpResponse,render
from django.http import JsonResponse
todos=[{'{name':'elis',
        'id':1,
        'completed':False},
          {'name':'Paat',
           'id':2,
           'completed':False}]
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
def update_todo(request,todoId):
    todo= None
    for i in todos:
        if i['id'] is todoId:
            todo=i
            break
    if todo is not None:
        todo['completed']=True
        return JsonResponse(todos, safe=False)
def delete_todo(request,todoId):
    todo= None
    for i in todos:
        if i['id'] is todoId:
            todo=i
            break
    if todo is not None:
        todos.remove(todo)
        return JsonResponse(f"Todo with id {todoId} deleted", safe=False)
    else:
        return JsonResponse(todos,safe=False)