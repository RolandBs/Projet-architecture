from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
# TODO function pour envoyer la view a react