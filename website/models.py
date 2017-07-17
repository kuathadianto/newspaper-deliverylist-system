from django.db import models

# Bild: speichert die Bilder für die Zusatzinformationen
class Bild(models.Model):
    datei = models.CharField(max_length=200)


# Straße: speichert die Straßenname
class Strasse(models.Model):
    strassenname = models.CharField(max_length=100)


# Zustellung: speichert die Information, wie viele Zeitungen pro Haus zu liefern
class Zustellung(models.Model):
    hausnummer = models.IntegerField()
    summe_zeitungen = models.IntegerField()
    strasse = models.ForeignKey(Strasse, on_delete=models.CASCADE)


# Zusatztext: da bei Zusatzinformationen gleichen Text benutzt,
#             existiert dieses Model.
class Zusatztext(models.Model):
    text = models.CharField(max_length=500)


# Zusatzinformation: speichert die Zusatzinformationen für jede Zustellung
class Zusatzinformation(models.Model):
    # nur Beschreibung, wird nicht in der Webseite gezeigt
    beschreibung = models.CharField(max_length=500)
    information = models.ForeignKey(Zusatztext, on_delete=models.CASCADE)
    bild = models.ForeignKey(Bild, on_delete=models.CASCADE)
    zustellung = models.ForeignKey(Zustellung, on_delete=models.CASCADE)
