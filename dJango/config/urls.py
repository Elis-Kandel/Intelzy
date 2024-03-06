from django.contrib import admin
from django.urls import path
from .views import func,hello_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hell/", hello_view),
    path('func/', func),
]
