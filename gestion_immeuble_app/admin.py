from django.contrib import admin
from . import models
from django.contrib.auth.models import Group

# Register your models here.


admin.site.register(models.Charge)
admin.site.register(models.FormulaireCharge)
admin.site.register(models.FormulaireListeDesProprietaires)
admin.site.register(models.FormulaireCotization)
admin.site.register(models.FormulairePConcierge)