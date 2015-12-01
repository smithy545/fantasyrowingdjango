from django.shortcuts import render, get_object_or_404

from .models import Athlete

def index(request):
    rower_list = Athlete.objects.all()[0:50]
    context = {'rower_list': rower_list}
    return render(request, 'viewathlete/index.html', context)

def detail(request, rower_id):
    rower = get_object_or_404(Athlete, pk=rower_id)
    refer_id = int(rower_id) / 50 + 1
    context = {'rower':rower, 'referrent':refer_id}
    return render(request, 'viewathlete/detail.html', context)

def rower_page(request, page_id):
    rower_list = Athlete.objects.all()[50*int(page_id)-50:50*int(page_id)]
    next_page = int(page_id) + 1
    last_page = int(page_id) - 1
    max_page = 1 + len(Athlete.objects.all()) / 50
    page = {'next':next_page, 'last':last_page, 'max':max_page, 'id':page_id}
    context = {'rower_list':rower_list, 'page':page}
    return render(request, 'viewathlete/page.html', context)
