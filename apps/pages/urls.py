from django.urls import path
from .views import PagesView
from .views_misc import MiscPagesView



urlpatterns = [
    path(
        "pages/account_settings/account/",
        PagesView.as_view(template_name="pages_account_settings_account.html"),
        name="pages-account-settings-account",
    ),
    path(
        "pages/account_settings/notifications/",
        PagesView.as_view(template_name="pages_account_settings_notifications.html"),
        name="pages-account-settings-notifications",
    ),
    path(
        "pages/account_settings/connections/",
        PagesView.as_view(template_name="pages_account_settings_connections.html"),
        name="pages-account-settings-connections",
    ),
    path(
        "pages/misc/error/",
        MiscPagesView.as_view(template_name="pages_misc_error.html"),
        name="pages-misc-error",
    ),
    path(
        "pages/misc/under_maintenance/",
        MiscPagesView.as_view(template_name="pages_misc_under_maintenance.html"),
        name="pages-misc-under-maintenance",
    )
]
