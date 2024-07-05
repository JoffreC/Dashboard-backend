from django.urls import path, include

urlpatterns = [
    path('author', include('apps.dashboards.infrastructure.api.v1.urls.author_urls'), name='authors'),
    path('affiliation/', include('apps.dashboards.infrastructure.api.v1.urls.affiliation_urls'), name='affiliation'),
    path('province/', include('apps.dashboards.infrastructure.api.v1.urls.province_urls'), name='province'),
    path('update-dashboard',include('apps.dashboards.infrastructure.api.v1.urls.update_urls'), name='updates'),
    path('country/', include('apps.dashboards.infrastructure.api.v1.urls.country_urls'), name='country'),
    path('general/', include('apps.dashboards.infrastructure.api.v1.urls.general_urls'), name='country'),
]