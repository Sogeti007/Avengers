from django.shortcuts import render
from django.db.models import Max
from .models import Winner



def home(request):
    winners = Winner.object.all()
    num_players = winners.count()
    best_player = winners.aggregate(Max('times_won'))
    #this_player = winners.filter(winner=).first()
    context = {
        'title': 'This',
        'num_players': num_players,
        'best_player': best_player,
        'winners': winners,
    }
    return render(request, 'main/main.html', context)
