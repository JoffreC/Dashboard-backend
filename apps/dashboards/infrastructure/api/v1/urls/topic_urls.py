from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.dashboards.infrastructure.api.v1.views.topic_views import TopicViewSet

router = DefaultRouter()
router.register(r'province', TopicViewSet, basename='topics')
urlpatterns = [
    path('', TopicViewSet.as_view({'get': 'retrieve'}), name='topics'),

]