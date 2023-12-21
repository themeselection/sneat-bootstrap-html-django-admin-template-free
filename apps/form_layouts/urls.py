from django.urls import path
from .views import FormLayoutsView



urlpatterns = [
    path(
        "form/layouts_vertical/",
        FormLayoutsView.as_view(template_name="form_layouts_vertical.html"),
        name="form-layouts-vertical",
    ),
    path(
        "form/layouts_horizontal/",
        FormLayoutsView.as_view(template_name="form_layouts_horizontal.html"),
        name="form-layouts-horizontal",
    )
]
