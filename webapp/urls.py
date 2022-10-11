# URLs

# Imports
from django.urls import path
from .views import HomeView

# Nome da app
app_name = "webapp"

# URL da página home
urlpatterns = [path("", HomeView.as_view(), name="home-view")]