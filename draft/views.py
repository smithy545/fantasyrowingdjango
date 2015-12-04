from django.shortcuts import render
from django.http import HttpResponse
import simplejson

def main(request):
    return render(request, 'draft/main.html', {})

def league_get_available(request):
	league = request.user.members.first()
	return HttpResponse(simplejson.dumps([a.get_full_name() for a in league.available_athletes()]))