from django.db import models

class Athlete(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    height = models.IntegerField("Height (cm)", null=True)
    weight = models.FloatField("Weight (kg)", null=True)
    gender = models.CharField(max_length=1, null=True)
    residence = models.CharField(max_length=200, null=True)
    clubs = models.CharField(max_length=500, null=True)
    started_rowing = models.IntegerField(default=2000, null=True)
    birth_date = models.DateField(null=True)

    def __unicode__(self):
        return self.last_name + u", " + self.first_name
