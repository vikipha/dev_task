from django.urls import path

from service.web.views import IndexView

app_name = "web"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
