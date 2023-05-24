from django.urls import path
from data.views import HomeView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
]