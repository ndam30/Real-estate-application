from django.shortcuts import render
from listings.choices import bedroom_choices,price_choices
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.

def index(request):
    listings =Listing.objects.filter(is_published=True).order_by('-list_date')
    context = {
        'listings':listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'home.html', context)

def about(request):

    realtors = Realtor.objects.order_by('hire_date')

    mvp_realters =Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtors': mvp_realters
    }
    return render(request, 'about.html' , context)

