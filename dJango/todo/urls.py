from django.urls import path
from .views import todo,read_todo,update_todo,delete_todo
urlpatterns = [
    path('<int:todoId>/',read_todo),
    path('<int:todoId>/update/',update_todo),
    path('<int:todoId>/delete/',delete_todo),
]
