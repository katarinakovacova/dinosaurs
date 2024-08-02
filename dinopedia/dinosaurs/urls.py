from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register("dinosaurs", views.DinosaurViewSet)
router.register("users", views.UserViewSet)
