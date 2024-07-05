from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.dashboards.infrastructure.api.v1.views.author_views import AuthorViewsSet

router = DefaultRouter()
router.register(r'', AuthorViewsSet, basename='author-dashboard')
urlpatterns = [
    path('', AuthorViewsSet.as_view({'get': 'retrieve'}), name='author-dashboard'),
]
