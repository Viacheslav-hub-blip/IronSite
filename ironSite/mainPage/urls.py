from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('politics', views.politics),
    path('about-us', views.aboutUs),
    path('creators', views.creators),
    path('Investors', views.investors),
]
