from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.dashboards.infrastructure.api.v1.views.country_views import CountryViewsSet

router = DefaultRouter()
router.register(r'country', CountryViewsSet, basename='country-dashboard')
urlpatterns = [
    path('list', CountryViewsSet.as_view({'get': 'list'}), name='country-years'),
    path('retrieve', CountryViewsSet.as_view({'get': 'retrieve'}), name='country-topics'),
]