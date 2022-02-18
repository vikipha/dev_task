from django.urls import path, include

urlpatterns = [path("", include("service.web.urls"))]
