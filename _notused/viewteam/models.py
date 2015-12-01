from django.db import models
from viewathlete.models import Athlete

class Team(models.Model):
    user = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    team_members = models.ManyToManyField(Athlete)

    def __unicode__(self):
        return self.name + u", " + self.user
