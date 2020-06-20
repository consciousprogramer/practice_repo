from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("addtask", views.addtask, name = "addtask"),
    #path("updatetask", views.updatetask, name = "updatetask")

]
