from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.dashboards.infrastructure.api.v1.views.country_views import CountryViewsSet

router = DefaultRouter()
router.register(r'', CountryViewsSet, basename='country-dashboard')
urlpatterns = [
    path('', include(router.urls)),
]
