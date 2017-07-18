from django.db import models

# Bild: speichert die Bilder für die Zusatzinformationen
class Bild(models.Model):
    titel = models.CharField(max_length=100, unique=True)
    datei = models.CharField(max_length=200) # Should be changed to image type

    def __str__(self):
        return self.titel


# Straße: speichert die Straßenname
class Strasse(models.Model):
    strassenname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.strassenname


# Zusatztext: da bei Zusatzinformationen gleichen Text benutzt,
#             existiert dieses Model.
class Zusatztext(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


# Zusatzinformation: speichert die Zusatzinformationen für jede Zustellung
class Zusatzinformation(models.Model):
    # nur Beschreibung, wird nicht in der Webseite gezeigt
    beschreibung = models.CharField(max_length=500, blank=True, null=True)
    information = models.ForeignKey(Zusatztext, on_delete=models.CASCADE)
    bild = models.ForeignKey(Bild, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.beschreibung + ': ' + self.information.text


# Zustellung: speichert die Information, wie viele Zeitungen pro Haus zu liefern
class Zustellung(models.Model):
    hausnummer = models.IntegerField()
    summe_zeitungen = models.IntegerField()
    strasse = models.ForeignKey(Strasse, on_delete=models.CASCADE)
    zusatzinformationen = models.ManyToManyField(Zusatzinformation)

    def __str__(self):
        return self.strasse.strassenname + ' ' + str(self.hausnummer)

    class Meta:
        unique_together = ('hausnummer', 'strasse')
