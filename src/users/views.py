from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.urls import reverse
from main.views import get_main_context
from django.contrib.auth import views as auth_views

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account für {username} angelegt, melde dich doch gleich an!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = get_main_context()
    context["form"] = form
    return render(request, 'users/register.html', context)


class LoginView(auth_views.LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_main_context())
        return context

class LogoutView(auth_views.LogoutView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_main_context())
        return context