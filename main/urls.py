from django.urls import path
from .views import HomePageView,TomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about", HomePageView.as_view(), name="about"),
    path("index", TomePageView, name="index"),
]
