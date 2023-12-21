from django.urls import path
from .views import IconsView



urlpatterns = [
    path(
        "icons/boxicons/",
        IconsView.as_view(template_name="icons_boxicons.html"),
        name="icons-boxicons",
    )
]
