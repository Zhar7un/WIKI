from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("service:get_random_page", views.random_entry, name="random_page"),
    path("service:search", views.search_entry, name="search"),
    path("<str:title>", views.render_page, name="render_page")
]
