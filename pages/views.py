from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views import View

from .forms import  LoginForm









from django.views.decorators.http import require_POST
import json
#


def property_detail(request):
  #listing = get_object_or_404(PropertyList, pk=listing_id)
  #photos = PhotoForListing.objects.order_by('description').filter(listing=listing_id) # order_by( #).get_object_or_404(PropertyList, pk=listing_id)
  context = {
  #  'property': listing,
   # 'photos': photos
  }


  return render(request, 'pages/property-detail.html',  context) 





from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.

