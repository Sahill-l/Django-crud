from django.urls import path
from .views import *
urlpatterns = [
    path("",Home,name="home"),
    path("add_student/",add_Student,name="add_student"),
    path("delete",delete,name="delete"),
    path("edit/<int:id>/",edit,name="edit")
]