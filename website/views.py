from django.shortcuts import render
from .models import Zustellung, Option
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    # Summe aller Zeitungen
    summe_zeitungen = Zustellung.objects.aggregate(Sum('summe_zeitungen'))['summe_zeitungen__sum']
    # Detaillierte der Zustellung
    zustellungen = Zustellung.objects.all()
    # Optionen
    standard_nachricht = '(nicht vorhanden)'
    zustellername = standard_nachricht
    bezirk = standard_nachricht
    letzte_aenderung = standard_nachricht
    try:
        zustellername = Option.objects.get(name='zustellername').wert
    except ObjectDoesNotExist:
        pass
    try:
        bezirk = Option.objects.get(name='bezirk').wert
    except ObjectDoesNotExist:
        pass
    try:
        letzte_aenderung = Option.objects.get(name='letzte_aenderung').wert
    except ObjectDoesNotExist:
        pass

    context = {
        'summe_zeitungen': summe_zeitungen,
        'zustellungen': zustellungen,
        'zustellername': zustellername,
        'bezirk': bezirk,
        'letzte_aenderung': letzte_aenderung,
    }
    return render(request, 'website/index.html', context)
