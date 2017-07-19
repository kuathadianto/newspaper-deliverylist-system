from django.test import TestCase
from django.db.utils import IntegrityError
from django.db import transaction
from .models import *

class Eindeutigkeitstest(TestCase):
    def setUp(self):
        # Eindeutigkeit von Strassen
        str_j = Strasse.objects.create(strassenname="Junkerstr.")
        try:
            with transaction.atomic():
                Strasse.objects.create(strassenname="Junkerstr.")
            self.fail("Es gibt Strassen mit gleichen Namen!")
        except IntegrityError:
            pass
        str_m = Strasse.objects.create(strassenname="Maastrichter Str.")

        # Eindeutigkeit von der Adresse der Zustellungen
        zt = Zustellung.objects.create(hausnummer = 54, summe_zeitungen = 10, strasse = str_j)
        Zustellung.objects.create(hausnummer = 54, summe_zeitungen = 10, strasse = str_m)
        try:
            with transaction.atomic():
                Zustellung.objects.create(hausnummer = 54, summe_zeitungen = 10, strasse = str_j)
            self.fail("Es gibt eine Zustellung mit der gleichen Adresse!")
        except IntegrityError:
            pass

        zus_t = Zusatztext.objects.create(text = "Darf hier nicht liefern!")

        # Bei Zusatzinformation darf die Beschreibung und das Bild leer sein
        Zusatzinformation.objects.create(information=zus_t, zustellung=zt)

        # Bei Optionnamen darf nicht gleich sein
        Option.objects.create(name="Test", wert="12345")
        try:
            with transaction.atomic():
                Option.objects.create(name="Test", wert="12345")
            self.fail("Es gibt Optionen mit gleichen Namen!")
        except IntegrityError:
            pass

    def test(self):
        self.assertTrue(True)
