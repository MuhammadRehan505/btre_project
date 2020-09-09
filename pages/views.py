from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices , bedroom_choices , state_choices    
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] #is_published means we only want to show ones that are true. [:3]means that we only want 3 listings
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices' : bedroom_choices, 
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context) 

def about(request):
    #get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    #get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True) #is_mvp=true only grab the ones that are true
  
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
  
    return render(request, 'pages/about.html', context)    