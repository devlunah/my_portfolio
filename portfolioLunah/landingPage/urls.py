from django.urls import path

from views import TemplateView

urlpatterns = [
    path("", views.index, name="index"),
]