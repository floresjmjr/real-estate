from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import state_choices, price_choices, bedroom_choices

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  # inside_pictures = []
  # for i in range(5):
    # if listing["photo_" + str(i)]:
      # inside_pictures.append(listing["photo_" + str(i)])

  context = { 
    "listing": listing,
    # "inside_pictures": inside_pictures,
  }

  return render(request, 'listings/listing.html', context)

def search(request):

  context = {
    "bedroom_choices": bedroom_choices,
    "state_choices": state_choices,
    "price_choices": price_choices,
  }

  return render(request, 'listings/search.html', context)