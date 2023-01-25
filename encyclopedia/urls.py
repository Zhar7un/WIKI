from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_random_page", views.random_entry, name="random_page"),
    path("<str:title>", views.render_page, name="render_page")
]
