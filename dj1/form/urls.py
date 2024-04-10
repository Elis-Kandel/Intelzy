from django.urls import path
from .views import index,delete,update,read,list
 
urlpatterns = [
 
    # path('',index),
    path('',list),
    path('<int:updateId>/delete/',delete),
    path('<int:updateId>/update/',update),
    path('<int:updateId>/read/',read),
    
]
