from django.db import models
from django.utils import timezone


class StateData(models.Model):
    state = models.CharField(max_length=50)
    cases = models.IntegerField()
    deaths = models.IntegerField()

    def __str__(self):
        return self.state


class CountyData(models.Model):
    cdate = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    cases = models.IntegerField()
    deaths = models.IntegerField()

    def __str__(self):
        return self.state + self.county
