from django.contrib import admin
from apps.muchos_a_muchos.models import Publication, Article

# Register your models here.
admin.site.register(Publication)
admin.site.register(Article)
