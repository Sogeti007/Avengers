from django.shortcuts import render
from django.db.models import Max
from django.contrib.auth.models import User
from datetime import date

def get_main_context():
    users = User.objects.all()

    num_users = users.count()
    if num_users > 0:
        today_registered = users.filter(date_joined__day=date.today().day).count()
        latest_user_name = users.latest('date_joined').get_username()
    else:
        today_registered = 0
        latest_user_name = ""

    return {
        'num_users': num_users,
        'today_registered': today_registered,
        'latest_user_name': latest_user_name,
    }


def home(request):
    return render(request, 'main/main.html', get_main_context())
