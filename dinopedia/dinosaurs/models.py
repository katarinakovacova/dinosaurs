from django.db import models
from django.utils.translation import gettext_lazy as _


class Dinosaur(models.Model):
    class EatingClassification(models.TextChoices):
        HERBIVORE = "H", _("Herbivore")
        OMNIVORE = "O", _("Omnivore")
        CARNIVORE = "C", _("Carnivore")
        UNKNOWN = "U", _("Unknown")

    class Period(models.TextChoices):
        TRIASSIC = "T", _("Triassic")
        JURASSIC = "J", _("Jurassic")
        CRETACEOUS = "C", _("Cretaceous")
        PALEOGENE = "P", _("Paleogene")
        NEOGENE = "N", _("Neogene")
        UNKNOWN = "U", _("Unknown")

    class Size(models.TextChoices):
        TINY = "XXS", _("Tiny")
        VERY_SMALL = "XS", _("Very small")
        SMALL = "S", _("Small")
        MEDIUM = "M", _("Medium")
        LARGE = "L", _("Large")
        VERY_LARGE = "XL", _("Very large")
        GIGANTIC = "XXL", _("Gigantic")
        UNKNOWN = "U", _("Unknown")
    
    name = models.CharField(max_length=150)
    eating_classification = models.CharField(max_length=1, choices=EatingClassification, default=EatingClassification.UNKNOWN)
    typical_color = models.CharField(max_length=50)
    period = models.CharField(max_length=1, choices=Period, default=Period.UNKNOWN)
    average_size = models.CharField(max_length=3, choices=Size, default=Size.UNKNOWN)

    
