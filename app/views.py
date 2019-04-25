from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from app.forms import SignUpForm


class SignUpPage(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})


class HomePage(View):

    def get(self, request):
        return render(request, 'home.html', {})

