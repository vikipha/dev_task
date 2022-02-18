from typing import Optional

from django.db import connection
from django.db.models import QuerySet
from django.views.generic import DetailView


class IndexView(DetailView):
    template_name = "web/index.html"

    def get_object(self, queryset: Optional[QuerySet] = None) -> None:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone()[0]
