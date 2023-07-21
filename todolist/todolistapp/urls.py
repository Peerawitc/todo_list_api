from django.urls import path,include
from todolistapp import views
urlpatterns = [
    path("",views.index),
    path("get/",views.getData),
    path("add/",views.addWork),
    path("edit/",views.edit),
    path("detail/<id>/",views.detail),
    path("delete/<id>/",views.delete)

    
]
