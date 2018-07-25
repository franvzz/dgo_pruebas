from django.contrib import admin
from apps.uno_a_uno.models import Pet, Owner

# Register your models here.
admin.site.register(Owner)
admin.site.register(Pet)
