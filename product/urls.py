from django.urls import path, include
from product import views

urlpatterns = [
    path('latest/', views.LatestProductsList.as_view()),
]