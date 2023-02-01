from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    sport_name = models.CharField(max_length=100)
    participants = models.ManyToManyField(Athlete)

    def __str__(self):
        return self.name
