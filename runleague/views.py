from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
import collections, simplejson

# Create your views here.
from .models import *
from .forms import *

def has_team(user):
	if hasattr(user, 'team_set'):
		return len(user.team_set.all()) > 0
	return False

def owns_league(user):
	if hasattr(user, 'owner'):
		return len(user.owner.all()) > 0
	return False

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

@user_passes_test(has_team, login_url='/runleague/signin', redirect_field_name=None)
def team_add_athlete(request):
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
	return render(request, 'runleague/team_add_athlete.html', context)

@user_passes_test(has_team, login_url='/runleague/signin', redirect_field_name=None)
def team_remove_athlete(request):
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
	return render(request, 'runleague/team_remove_athlete.html', context)

@user_passes_test(has_team, login_url='/runleague/signin', redirect_field_name=None)
def team_trade_athlete(request):
	if request.method == "GET":
		form = TradePlayerForm(request.user) 
	elif request.method == "POST":
		form = TradePlayerForm(request.user, request.POST)
		return render(request, 'runleague/team_trade_sent.html', {})
	return render(request, 'runleague/team_trade_athlete.html', {'form':form})

def team_get_athletes(request, teamid):
	if request.GET.get('teamid'):
		teamid = request.GET.get('teamid')
		athletes = [unicode(a) for a in Team.objects.get(pk=teamid).athletes.all()]
	else:
		athletes = None
	
	if not athletes:
		athletes = ["No athletes"]

	return HttpResponse(simplejson.dumps(athletes))
	
@user_passes_test(has_team, login_url='/runleague/signin', redirect_field_name=None)
def team_edit_name(request):
	if request.method == "GET":
		form = EditNameForm()
	elif request.method == "POST":
		form = EditNameForm(request.POST)
		if form.is_valid():
			t = request.user.team_set.first()
			t.name = form.cleaned_data['name']
			t.save()
			return redirect('/runleague/team')
	return render(request, 'runleague/team_edit_name.html', {'form':form, 'team':request.user.team_set.first()})
	
@user_passes_test(has_team, login_url='/runleague/signin', redirect_field_name=None)
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
	return render(request, 'runleague/team_detail.html', context)

@user_passes_test(has_team, login_url='/runleague/signin', redirect_field_name=None)
def athlete_remove(request, athlete_id):
	team = request.user.team_set.first()
	athlete = Athlete.objects.get(pk=athlete_id)
	if athlete in team.athletes.all():
		team.athletes.remove(athlete)
	not_added = team.league.available_athletes()
	context = {'team':team, 'not_added':not_added}
	return render(request, 'runleague/team_detail.html', context)

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

@user_passes_test(owns_league, login_url='/runleague/league_detail', redirect_field_name=None)
def league_edit(request):
	league = request.user.owner.first()
	referer = u'/' + u'/'.join(request.META.get('HTTP_REFERER').split('/')[3:])
	return render(request, 'runleague/league_edit.html', {'league':league, 'referer':referer})

@user_passes_test(has_team, login_url='/runleague/league_detail', redirect_field_name=None)
def league_kick_user(request, user_id):
	u = User.objects.get(pk=user_id)
	l = request.user.members.first()

	if u.id != request.user.id and l.owner != request.user.id:
		return redirect("/runleague/league")
	
	if len(l.members.all()) <= 1:
		l.delete()
	elif l.owner == u:
		l.members.remove(u)
		l.owner = l.members.first()
		l.save()
	else:
		l.members.remove(u)
		l.save()

	if u.team_set.first():
		u.team_set.first().delete()
	return render(request, 'runleague/user_kicked.html', {'user':u, 'league':l})

def make_team(request):
	if request.method == 'GET':
		form = ChooseLeagueForm()
	elif request.method == 'POST':
		form = ChooseLeagueForm(request.POST)
		if form.is_valid():
			l = form.cleaned_data.get('league')
			teamname = form.cleaned_data.get('teamname')
			request.user.team_set.add(Team(user = request.user, name=teamname, league=l))
			request.user.members.add(l)
			return render(request, 'runleague/make_team_success.html', {})
	return render(request, 'runleague/make_team.html', {'form':form})

def new_league(request):
	if request.method == 'GET':
		form = LeagueForm()
	elif request.method == 'POST':
		form = LeagueForm(request.POST)
		if form.is_valid():
			l = form.save(commit=False)
			l.owner = request.user
			l.save()
			request.user.members.add(l)
			request.user.team_set.add(Team(user = request.user, name="Team " + str(request.user.username), league=l))
			context = {}
			return render(request, 'runleague/make_league_success.html', context)
	return render(request, 'runleague/newleague.html', {'form':form})

def draft(request):
	return render(request, 'runleague/draft.html', {})
