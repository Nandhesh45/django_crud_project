from django.urls import path

from new_app import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("",views.index,name="index"),
    path("dash",views.dash,name="dash"),
    path("data",views.furniture,name="data"),
    path("table",views.furniture_view,name="table"),
    path("delete/<int:id>/",views.furniture_delete,name="furniture_delete"),
    path("update/<int:id>/",views.furniture_update,name='furniture_update')
]