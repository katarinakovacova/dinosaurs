from django.urls import path

from . import views

urlpatterns = [
    path("api/v1/dinosaurs", views.dinosaurs_list),
    path("api/v1/dinosaurs/<int:pk>/", views.dinosaur_detail),
]
