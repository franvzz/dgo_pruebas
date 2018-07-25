from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pet(models.Model):
    # fields
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    admission = models.DateField(null=True, blank=True)
    # oneToMany
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
