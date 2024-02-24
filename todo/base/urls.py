from django.urls import path
from . import views

urlpatterns = [
    path("",views.taskList,name="home"),
    path("update/<str:pk>",views.taskUpdate,name="updateTask"),
]
