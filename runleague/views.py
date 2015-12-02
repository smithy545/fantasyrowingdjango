from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import collections

# Create your views here.
from .models import *
from .forms import *

class IndexView(generic.TemplateView):
	template_name = 'runleague/about.html'

class AboutView(generic.TemplateView):
	template_name = 'runleague/about.html'
	
class TeamSuccessView(generic.TemplateView):
	template_name = 'runleague/make_team_success.html'
		
class LeagueSuccessView(generic.TemplateView):
	template_name = 'runleague/make_league_success.html'
	
def team_detail(request, team_id):
	team = Team.objects.get(pk=team_id)
	referer = u'/' + u'/'.join(request.META.get('HTTP_REFERER').split('/')[3:])
	context = {'team':team, 'referer':referer}
	return render(request, 'runleague/team_detail.html', context)

def my_team_detail(request):
	if request.user.is_authenticated():
		team = request.user.team_set.first()
	else:
		team = None
	referer = u'/' + u'/'.join(request.META.get('HTTP_REFERER').split('/')[3:])
	context = {'team':team, 'referer':referer}
	return render(request, 'runleague/team_detail.html', context)

def team_page(request, page_id):
	team_list = Team.objects.all()[50*int(page_id)-50:50*int(page_id)]
	next_page = int(page_id) + 1
	last_page = int(page_id) - 1
	max_page = 1 + len(Team.objects.all()) / 50
	page = {'next':next_page, 'last':last_page, 'max':max_page, 'id':page_id}
	context = {'team_list':team_list, 'page':page}
	return render(request, 'runleague/team_page.html', context)
	
def team_edit(request):
	team = request.user.team_set.first()
	schools = Athlete.objects.order_by().values('school').distinct()
	not_added = {}
	for school in schools:
		temp = Athlete.objects.filter(school=school['school'])
		not_added[school['school']] = []
		for athlete in temp:
			if not (athlete in team.league.taken_athletes()):
				not_added[school['school']].append(athlete)
	not_added = collections.OrderedDict(sorted(not_added.items()))
	
	context = {'team':team, 'not_added':not_added}
	return render(request, 'runleague/team_edit.html', context)

def team_add_player(request):
	team = request.user.team_set.first()
	schools = Athlete.objects.order_by().values('school').distinct()
	not_added = {}
	for school in schools:
		temp = Athlete.objects.filter(school=school['school'])
		not_added[school['school']] = []
		for athlete in temp:
			if not (athlete in team.league.taken_athletes()):
				not_added[school['school']].append(athlete)
	not_added = collections.OrderedDict(sorted(not_added.items()))
	
	context = {'team':team, 'not_added':not_added}
	return render(request, 'runleague/team_add_player.html', context)

def team_remove_player(request):
	team = request.user.team_set.first()
	schools = Athlete.objects.order_by().values('school').distinct()
	not_added = {}
	for school in schools:
		temp = Athlete.objects.filter(school=school['school'])
		not_added[school['school']] = []
		for athlete in temp:
			if not (athlete in team.league.taken_athletes()):
				not_added[school['school']].append(athlete)
	not_added = collections.OrderedDict(sorted(not_added.items()))
	
	context = {'team':team, 'not_added':not_added}
	return render(request, 'runleague/team_remove_player.html', context)
	
def team_trade_player(request):
	team = request.user.team_set.first()
	schools = Athlete.objects.order_by().values('school').distinct()
	not_added = {}
	for school in schools:
		temp = Athlete.objects.filter(school=school['school'])
		not_added[school['school']] = []
		for athlete in temp:
			if not (athlete in team.league.taken_athletes()):
				not_added[school['school']].append(athlete)
	not_added = collections.OrderedDict(sorted(not_added.items()))
	
	context = {'team':team, 'not_added':not_added}
	return render(request, 'runleague/team_trade_player.html', context)
	
def athlete_add(request, athlete_id):
	team = request.user.team_set.first()
	athlete = Athlete.objects.get(pk=athlete_id)
	if not (athlete in team.league.taken_athletes()):
		team.athletes.add(athlete)
	not_added = {}
	schools = Athlete.objects.order_by().values('school').distinct()
	for school in schools:
		temp = Athlete.objects.filter(school=school['school'])
		not_added[school['school']] = []
		for athlete in temp:
			if not (athlete in team.league.taken_athletes()):
				not_added[school['school']].append(athlete)
	not_added = collections.OrderedDict(sorted(not_added.items()))
	
	context = {'team':team, 'not_added':not_added}
	return render(request, 'runleague/team_edit.html', context)
	
def athlete_remove(request, athlete_id):
	team = request.user.team_set.first()
	athlete = Athlete.objects.get(pk=athlete_id)
	if athlete in team.athletes.all():
		team.athletes.remove(athlete)
	not_added = team.league.available_athletes()
	context = {'team':team, 'not_added':not_added}
	return render(request, 'runleague/team_edit.html', context)
	
def athlete_detail(request, athlete_id):
	rower = get_object_or_404(Athlete, pk=athlete_id)
	referer = u'/' + u'/'.join(request.META.get('HTTP_REFERER').split('/')[3:])
	context = {'rower':rower, 'referer':referer}
	return render(request, 'runleague/athlete_detail.html', context)

def athlete_page(request, page_id):
	rower_list = Athlete.objects.all()[50*int(page_id)-50:50*int(page_id)]
	next_page = int(page_id) + 1
	last_page = int(page_id) - 1
	max_page = 1 + len(Athlete.objects.all()) / 50
	page = {'next':next_page, 'last':last_page, 'max':max_page, 'id':page_id}
	context = {'rower_list':rower_list, 'page':page}
	return render(request, 'runleague/athlete_page.html', context)

def sign_in(request):
	if request.method == 'GET':
		form = LoginForm()
		message = ''
	elif request.method == 'POST':
		message = 'Invalid credentials'
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = 'Login successful'
	return render(request, 'runleague/signin.html', {'form':form, 'message':message})
	
def sign_out(request):
	logout(request)
	return render(request, 'runleague/signout.html',{})
	
def sign_up(request):
	if request.method == 'GET':
		form = SignupForm()
	elif request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			return render(request, 'runleague/signin.html', {'form':LoginForm(),'message':str(user)+" successfully created"})
	return render(request, 'runleague/signup.html', {'form':form})

def league_detail(request, league_id):
	league = League.objects.get(pk=league_id)
	referer = u'/' + u'/'.join(request.META.get('HTTP_REFERER').split('/')[3:])
	context = {'league':league, 'referer':referer}
	return render(request, 'runleague/league_detail.html', context)

	
def my_league_detail(request):
	if hasattr(request.user, 'members'):
		league = request.user.members.first()
	else:
		league = None
	referer = u'/' + u'/'.join(request.META.get('HTTP_REFERER').split('/')[3:])
	context = {'league':league, 'referer':referer}
	return render(request, 'runleague/league_detail.html', context)

def make_team(request):
	if request.method == 'GET':
		form = ChooseLeagueForm()
	elif request.method == 'POST':
		form = ChooseLeagueForm(request.POST)
		if form.is_valid():
			league = form.cleaned_data.get('league')
			teamname = form.cleaned_data.get('teamname')
			l = League.objects.get(pk=league)
			request.user.team_set.add(Team(user = request.user, name=teamname, league=l))
			request.user.members.add(l)
			return render(request, 'runleague/make_team_success.html', {})
	return render(request, 'runleague/make_team.html', {'form':form})

def new_league(request):
	if request.method == 'GET':
		form = NewLeagueForm()
	elif request.method == 'POST':
		form = NewLeagueForm(request.POST)
		if form.is_valid():
			leaguename = form.cleaned_data.get('leaguename')
			leaguesize = form.cleaned_data.get('leaguesize')
			l = League(name=leaguename, leaguesize=leaguesize, owner=request.user)
			l.save()
			request.user.members.add(l)
			request.user.team_set.add(Team(user = request.user, name="Team " + str(request.user.username), league=l))
			context = {}
			return render(request, 'runleague/make_league_success.html', context)
	return render(request, 'runleague/newleague.html', {'form':form})

def draft(request):
	return render(request, 'runleague/draft.html', {})