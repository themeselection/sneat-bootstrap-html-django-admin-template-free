from django.urls import path
from .views import CardView



urlpatterns = [
    path(
        "cards/basic/",
      CardView.as_view(template_name="cards_basic.html"),
        name="cards-basic",
    )
]
