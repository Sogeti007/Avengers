from django.shortcuts import render
from django.db.models import Max
from django.contrib.auth.models import User
from datetime import date

def get_main_context():
    users = User.objects.all()
    num_users = users.count()

    today_registered = users.filter(date_joined__day=date.today().day).count()
    latest_user_name = users.latest('date_joined').get_username()
    # best_player = winners.aggregate(Max('times_won'))
    # #this_player = winners.filter(winner=).first()
    return {
        'num_users': num_users,
        'today_registered': today_registered,
        'latest_user_name': latest_user_name,
    }


def home(request):
    return render(request, 'main/main.html', get_main_context())
