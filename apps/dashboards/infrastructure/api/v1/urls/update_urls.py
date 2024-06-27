from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.dashboards.infrastructure.api.v1.views.update_view import UpdateView

router = DefaultRouter()
router.register(r'update', UpdateView, basename='update-dashboard')
urlpatterns = [
    path('', UpdateView.as_view(), name='update-dashboard'),
]