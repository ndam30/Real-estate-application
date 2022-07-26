from django.http import request
from django.shortcuts import render, get_object_or_404

from .choices import price_choices, bedroom_choices, state_choices
from .models import Listing
from django.core.paginator import Paginator

# Create your views here.



def index(request):
    listings = Listing.objects.order_by('list_date')
    paginator = Paginator(listings,3)
    page =request.GET.get('page')
    paged_list =paginator.get_page(page)
    context = {
         'listings': paged_list
     }
    return render(request, 'list/listings.html', context)


def list(request, listing_id):
    listed = get_object_or_404(Listing, pk = listing_id)
    context = {
        'listed':listed
    }
    return render(request, 'list/list.html', context )

def search(request):
        queryset_list = Listing.objects.order_by('-list_date')

        # Keywords
        if 'keywords' in request.GET:
            keywords = request.GET['keywords']
            if keywords:
                queryset_list = queryset_list.filter(description__icontains=keywords)

        # City
        if 'city' in request.GET:
            city = request.GET['city']
            if city:
                queryset_list = queryset_list.filter(city__icontains=city)

        # State
        if 'state' in request.GET:
            state = request.GET['state']
            if state:
                 queryset_list = queryset_list.filter(state__iexact=state)

        # Bedrooms
        if 'bedrooms' in request.GET:
            bedrooms = request.GET['bedrooms']
            if bedrooms:
                queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

        # Price
        if 'price' in request.GET:
            price = request.GET['price']
            if price:
                queryset_list = queryset_list.filter(price__lte=price)

        context = {
            'state_choices': state_choices,
            'bedroom_choices': bedroom_choices,
            'price_choices': price_choices,
            'listings': queryset_list,
            'values': request.GET
        }

        return render(request, 'list/search.html', context)



