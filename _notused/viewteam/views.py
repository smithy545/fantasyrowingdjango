from django.shortcuts import render, get_object_or_404

from .models import Team
from viewathlete.models import Athlete

def index(request):
    team_list = Team.objects.all()[0:50]
    context = {'team_list': team_list}
    return render(request, 'viewteam/index.html', context)

def detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    refer_id = int(team_id) / 50 + 1
    context = {'team':team, 'referrent':refer_id}
    return render(request, 'viewteam/detail.html', context)

def team_page(request, page_id):
    team_list = Team.objects.all()[50*int(page_id)-50:50*int(page_id)]
    next_page = int(page_id) + 1
    last_page = int(page_id) - 1
    max_page = 1 + len(Team.objects.all()) / 50
    page = {'next':next_page, 'last':last_page, 'max':max_page, 'id':page_id}
    context = {'team_list':team_list, 'page':page}
    return render(request, 'viewteam/page.html', context)

def edit(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    not_added = Athlete.objects.all()
    refer_id = int(team_id) / 50 + 1
    context = {'team':team, 'not_added':not_added, 'referrent':refer_id}
    return render(request, 'viewteam/edit.html', context)
