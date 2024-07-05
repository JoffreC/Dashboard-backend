from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.dashboards.infrastructure.api.v1.views.general_dashboard_views import GeneralDashboardView

router = DefaultRouter()
router.register(r'', GeneralDashboardView, basename='general-dashboard')
urlpatterns = [
    path('retrieve/', GeneralDashboardView.as_view({'get': 'retrieve'}), name='general-dashboard'),
]
