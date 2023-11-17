from django.shortcuts import render
from .models import Listing

# Create your views here.

# CRUD - create, retrieve, update, delete, list

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings":listings
    }
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing":listing
    }
    return render(request, "listing.html", context)