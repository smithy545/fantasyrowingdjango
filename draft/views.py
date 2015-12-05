from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
import simplejson

def main(request):
    return render(request, 'draft/main.html', {})

def league_get_available(request):
	league = request.user.members.first()
	return HttpResponse(serialize('json', league.available_athletes()))

def league_get_players(request):
	league = request.user.members.first()
	return HttpResponse(serialize('json', league.schedule.get_players()))
	