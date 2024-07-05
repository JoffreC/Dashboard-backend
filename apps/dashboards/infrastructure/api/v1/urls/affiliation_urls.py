from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.dashboards.infrastructure.api.v1.views.affiliation_view import AffiliationViewSet

router = DefaultRouter()
router.register(r'', AffiliationViewSet, basename='affiliation-dashboard')
urlpatterns = [
    path('list', AffiliationViewSet.as_view({'get': 'list'}), name='affiliations-dashboard'),
    path('retrieve', AffiliationViewSet.as_view({'get': 'retrieve'}), name='affiliation-dashboard'),
    path('', include(router.urls)),
]
