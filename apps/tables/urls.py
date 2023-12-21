from django.urls import path
from .views import TableView



urlpatterns = [
    path(
        "tables/basic/",
        TableView.as_view(template_name="tables_basic.html"),
        name="tables-basic",
    )
]
