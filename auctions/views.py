from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing


def index(request):
    return render(request, "auctions/index.html")

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

def create_listing(request):
    assert isinstance(request, HttpRequest)
    if (request.method == "POST"):
        # Process following
        # 1. Title of listing
        # 2. Text based description
        # 3. Starting bid
        # 4. Image URL
        # 5. Category: fashion/toys/electronics/furniture etc.'''
        
        title = request.POST["title"]
        description = request.POST["description"]
        bid = request.POST["bid"]
        imgurl = request.POST["imgurl"]
        category = request.POST["category"]

        listing = Listing(title=title, desciption=description, bid=bid, imgurl=imgurl, category=category)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create_listing.html")