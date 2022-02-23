# Load path from django.urls
from django.urls import path
# Load this application views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get index view
    # Examples url: /airports/
    path('/', views.index),
    # Show Airport info
    # Example url /airports/MYR
    # Notice: the airport_code parameter in the url matches
    #   the parameter in the airport_info function
    path('/<str:airport_code>', views.airport_info),
]