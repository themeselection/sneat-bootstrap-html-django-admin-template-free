from django.urls import path
from .views import (
    WithoutMenuView,
    WithoutNavView,
    FluidView,
    ContainerView,
    BlankView,
)


urlpatterns = [
    path(
        "layouts/without_menu/",
        WithoutMenuView.as_view(template_name="layouts_without_menu.html"),
        name="layouts-without-menu",
    ),
    path(
        "layouts/without_navbar/",
        WithoutNavView.as_view(template_name="layouts_without_navbar.html"),
        name="layouts-without-navbar",
    ),
    path(
        "layouts/fluid/",
        FluidView.as_view(template_name="layouts_fluid.html"),
        name="layouts-fluid",
    ),
    path(
        "layouts/container/",
        ContainerView.as_view(template_name="layouts_container.html"),
        name="layouts-container",
    ),
    path(
        "layouts/blank/",
        BlankView.as_view(template_name="layouts_blank.html"),
        name="layouts-blank",
    ),
]
