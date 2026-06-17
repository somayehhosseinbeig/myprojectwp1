from django.shortcuts import render
from .models import *
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights":Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(), # pyright: ignore[reportAttributeAccessIssue]
    })

def book(request, flight_id):
    if request.method == "POST":
        try:
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
      
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,))) # pyright: ignore[reportAttributeAccessIssue]


