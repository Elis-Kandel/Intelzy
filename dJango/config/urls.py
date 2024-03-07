from django.contrib import admin
from django.urls import path
from .views import todo,read_todo

urlpatterns = [
    path('admin/', admin.site.urls),

    path('todos/', todo),
    path('todos/<int:todoId>/',read_todo)
    
]
