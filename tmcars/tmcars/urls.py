from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from products import views
from .settings import base

router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet, basename="Category")
router.register(r"locations", views.LocationViewSet, basename="Location")
router.register(r"products", views.ProductViewSet, basename="Product")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

if base.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    ]
