from django.contrib import admin
from apps.uno_a_muchos.models import Pet, Owner, Vaccine

# Register your models here.
admin.site.register(Owner)
admin.site.register(Vaccine)
admin.site.register(Pet)
