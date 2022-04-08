# Load path from django.urls
from django.urls import path
# Load this application views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get index view
    # Examples url: /flights/
    path('', views.index),
    # Show Flight search info
    # Example url /flights/search/MYR/LAX
    path('search/', views.search),
    path('search/<str:origin>/<str:destination>', views.flight_search),
    # added path week 11 assignment

]
