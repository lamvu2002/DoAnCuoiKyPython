from django.urls import path
from . import views

urlpatterns = [
    path("cthd/", views.table_cthd, name="cthd"),
    path('edit_cthd/<int:sohd>/<str:masp>/', views.edit_cthd, name='edit_cthd'),
    path('delete_cthd/<int:sohd>/<str:masp>/', views.delete_cthd, name='delete_cthd'),
    path('add_cthd/', views.add_cthd, name='add_cthd'),
]
