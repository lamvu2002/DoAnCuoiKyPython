from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("<int:makh>/", views.detail, name="detail"),

]