from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Athlete(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	school = models.CharField(max_length=200)
	age = models.IntegerField(default=18, null=True)
	height = models.FloatField("Height (cm)", max_length=20, null=True)
	weight = models.IntegerField("Weight (kg)", null=True)
	hometown = models.CharField(max_length=200, null=True)
	high_school = models.CharField(max_length=200, null=True)
	year = models.CharField(max_length=20,null=True)
	major = models.CharField(max_length=200,null=True)
	side = models.CharField(max_length=200,null=True)
	ranking = models.IntegerField(unique=True)

	def __unicode__(self):
		return self.last_name + u", " + self.first_name
	
	def get_height(self):
		return unicode(int(self.height)/12) + "'" + unicode(int(self.height)%12) + '"'
		
class LeagueManager(models.Manager):
	def open_leagues(self):
		openleagues = []
		for l in League.objects.all():
			if l.open and len(l.members.all()) < l.size:
				openleagues.append(l)
				
		return openleagues
		
class League(models.Model):
	name = models.CharField(max_length=200)
	members = models.ManyToManyField(User, related_name='members')
	owner = models.ForeignKey(User, related_name='owner')
	size = models.IntegerField(default=8, choices=[(6,6),(8,8),(10,10)])
	open = models.BooleanField(default=True)
	draft_start_date = models.DateTimeField()
	draft_end_date = models.DateTimeField()
	
	objects = LeagueManager()

	def __unicode__(self):
		return unicode(self.name)
		
	def available_athletes(self):
		return [a for a in Athlete.objects.all() if a not in self.taken_athletes()]
	
	def taken_athletes(self):
		athletes = []
		for team in self.team_set.all():
			athletes += team.athletes.all()
		return athletes

	@property
	def can_draft(self):
		if timezone.now() < self.draft_end_date and timezone.now() > self.draft_start_date:
			return True
		return False

class Team(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=200)
	league = models.ForeignKey(League)
	athletes = models.ManyToManyField(Athlete)

	def __unicode__(self):
		return self.name + u", " + self.user.username
