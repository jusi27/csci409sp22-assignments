from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from routes');


def routes_search(request, origin, destination):
    return HttpResponse('Showing routes from ' + origin + ' to ' + destination);
