from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from .models import Card


def index(request):
    cards_list = Card.objects.order_by('-value')
    context = {
        'cards_list': cards_list,
    }
    return render(request, 'cards/index.html', context)

def show(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/show.html', {'card': card })
