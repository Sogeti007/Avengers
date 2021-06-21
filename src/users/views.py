from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from main.views import get_main_context

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account für {username} angelegt, melde dich doch gleich an!")
            return redirect('login', get_main_context())
    else:
        form = UserRegisterForm()
    context = get_main_context()
    context["form"] = form
    return render(request, 'users/register.html', context)
