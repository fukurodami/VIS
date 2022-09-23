from django.urls import path
from school import views
from unicodedata import name

urlpatterns = [
    path("", views.MainView.as_view()),
    path("entry/", views.Entry.as_view()),
    path("<int:pk>/", views.SerialView.as_view()),
]