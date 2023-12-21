from django.urls import path
from .views import ExtendedUiView



urlpatterns = [
    path(
        "extended_ui/perfect_scrollbar/",
        ExtendedUiView.as_view(template_name="extended_ui_perfect_scrollbar.html"),
        name="extended-ui-perfect-scrollbar",
    ),
    path(
        "extended_ui/text_divider/",
        ExtendedUiView.as_view(template_name="extended_ui_text_divider.html"),
        name="extended-ui-text-divider",
    )
]
