from django.contrib import admin
from django.urls import path

from listings.views import (
    listing_list, 
    listing_retrieve, 
    listing_create, 
    listing_update
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list ),
    path('listings/<pk>/', listing_retrieve),
    path('listings/<pk>/edit/', listing_update),
    path('add-listing/', listing_create)
]
