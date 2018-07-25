from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pet(models.Model):
    # fields
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    admission = models.DateField(null=True, blank=True)
    # Many-to-one relationship
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=models.CASCADE)
    # ManyToMany
    vaccine = models.ManyToManyField(Vaccine)

    def __str__(self):
        return self.name
