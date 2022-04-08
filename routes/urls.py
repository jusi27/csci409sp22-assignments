# Load path from django.urls
from django.urls import path
# Load this application views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get index view
    # Examples url: /flights/
    path('', views.index),
    # Show Routes search info
    # Example url /routes/search/MYR/LAX

    path('search/<str:origin>/<str:destination>', views.routes_search),
]
