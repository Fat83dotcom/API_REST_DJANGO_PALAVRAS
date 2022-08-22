from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import viewsets


router = DefaultRouter()
router.register('palavra', viewsets.PalavraViewSet)

urlpatterns = [
    path('', include(router.urls))
]
