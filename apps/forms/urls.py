from django.urls import path
from .views import FormsView



urlpatterns = [
    path(
        "forms/basic_inputs/",
        FormsView.as_view(template_name="forms_basic_inputs.html"),
        name="forms-basic-inputs",
    ),
    path(
        "forms/input_groups/",
        FormsView.as_view(template_name="forms_input_groups.html"),
        name="forms-input-groups",
    )
]
