from . import views
from django.urls import path

urlpatterns = [
    # path('generate_checkout', views.generate_checkout, name='generate_checkout'),
    path('', views.index, name='index')
]

