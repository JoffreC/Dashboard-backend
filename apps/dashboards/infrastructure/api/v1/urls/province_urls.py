from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.dashboards.infrastructure.api.v1.views.province_views import ProvinceViewSet
router = DefaultRouter()
router.register(r'province', ProvinceViewSet, basename='province-dashboard')
urlpatterns = [
    path('list', ProvinceViewSet.as_view({'get': 'list'}), name='provinces-dashboard'),
    path('retrieve', ProvinceViewSet.as_view({'get': 'retrieve'}), name='province-dashboard'),
    path('', include(router.urls))
]
