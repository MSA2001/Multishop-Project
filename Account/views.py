from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
from django.views import View


class UserLoginView(View):
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'Account/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'invalid phone number/password', 'danger')
                return redirect('Account:user_login')
        return render(request, 'Account/login.html', {'form': form})
