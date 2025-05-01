from django.urls import path, include # type: ignore

urlpatterns = [
    path("api/", include("postmasterdjango_app_api.urls")),
]
