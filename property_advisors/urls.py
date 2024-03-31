from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from property.views import ContactView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("property.urls")),
    path("", include("users.api.urls", namespace="users_api")),
    path("", include("property.api.urls", namespace="property_api")),
    path("contact/", ContactView, name="contact"),
    path("accounts/", include("users.urls", namespace="users")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "property_advisors.views.page_not_found_view"
