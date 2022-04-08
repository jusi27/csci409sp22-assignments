# Load path from django.urls
from django.urls import path
# Load this application views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get index view
    # Examples url: /tickets/
    path('', views.index),
    # Show Tickets search info
    # Example url /tickets/123456789

    path('<int:confirmation_number>', views.ticket_search),
    # added path Week 11 Assignment
    path('search/', views.search),

]
