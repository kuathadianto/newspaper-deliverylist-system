from django.shortcuts import render
from .models import Zustellung
from django.db.models import Sum

def index(request):
    # Summe aller Zeitungen
    summe_zeitungen = Zustellung.objects.aggregate(Sum('summe_zeitungen'))['summe_zeitungen__sum']
    # Detaillierte der Zustellung
    zustellungen = Zustellung.objects.all()
    context = {
        'summe_zeitungen': summe_zeitungen,
        'zustellungen': zustellungen,
    }
    return render(request, 'website/index.html', context)
