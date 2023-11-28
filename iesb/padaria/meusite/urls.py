from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('produtos/', views.produtosList, name='lista_produtos'),
]
