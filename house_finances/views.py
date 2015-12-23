from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse,Http404
from .models import Roomie, Debt, Payment, Item


def index(request):
    roomies = Roomie.objects.all()
    return render(
        request,
        "house_finances/index.html", 
        {"roomies": roomies}
    )


def roommie_detail(request):
    id = request.GET.get("id", None)
    if id:
        roomie = get_object_or_404(Roomie, id=id)
        return render(
            request,
            "house_finances/roommie_detail.html",
            {"roomie": roomie}
        )


def item_list(request):
    item_list = Item.objects.all().order_by('-date_bought')
    paid_list = [item for item in item_list if item.paid_for]
    unpaid_list = [item for item in item_list if not item.paid_for]
    return render(
        request,
        "house_finances/item_list.html",
        {
            "paid_list": paid_list,
            "unpaid_list": unpaid_list
        }
    )

def item_detail(request):
    id = request.GET.get("id", None)
    if id:
        item = get_object_or_404(Item, pk=id)
        return render(
            request,
            "house_finances/item_detail.html",
            {
                "item": item,
            }
        )
    else:
        raise Http404
