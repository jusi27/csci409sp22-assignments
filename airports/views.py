from django.shortcuts import render
from .models import Airport


def index(request):
    # Fetch all airports form database
    airports = Airport.objects.all()
    # Create a displayable string. We will change this next week.
    # This is just to show some data.
    # airport_list = ', '.join([a.airport_code for a in airports])
    # return HttpResponse('Showing all airports: ' + airport_list)
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)


def airport_info(request, airport_code):
    # Fetch the airport by a certain code
    # Remember as we are only expecting one airport per code we should use get
    airport = Airport.objects.get(airport_code=airport_code)
    # Display the airport name and code
    context = {'airport': airport}
    return render(request, 'airports/airport.html', context)
    # return HttpResponse('Showing info for airport: ' + airport.name + "- " + airport.airport_code)
