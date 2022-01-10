from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from .models import *

from .models import User


def index(request):
    auctions = Auction.objects.all().order_by("-date_created")

    return render(request, "auctions/index.html", {'auctions': auctions})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new_listing(request):
    if request.method == "POST":
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.user = request.user
            auction.save()
            return redirect(('/'))
    else:
        form = AuctionForm()

        return render(request, 'auctions/new_listing.html', {'form': form})


def listing_page(request, auction_id):

    # Todo:
    # bid form
    # user checking
    auction = Auction.objects.get(id=auction_id)
    if request.method == 'POST':

        if auction.iswatch:
            message = 'already watched'
            return render(request, 'auctions/listing_page.html', {'auction': auction, 'message': message})

        else:
            auction.iswatch = True
            auction.save()

    return render(request, 'auctions/listing_page.html', {'auction': auction})


def watch_list(request):

    if request.method == 'POST':
        id = request.POST.get('id')
        x = Auction.objects.get(id=id)
        x.iswatch = False
        x.save()

    items = Auction.objects.filter(iswatch=True)

    return render(request, 'auctions/watch_list.html', {'items': items})
