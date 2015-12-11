from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from .models import Roomie, Debt, Payment, Item


def index(request):
    roomies = Roomie.objects.all()
    return render(
        request,
        "house_finances/index.html", 
        {"roomies": roomies}
    )


def detail(request):
    id = request.GET.get("id", None)
    if id:
        roomie = Roomie.objects.get(id=id)
        return render(
            request,
            "house_finances/detail.html",
            {"roomie": roomie}
        )