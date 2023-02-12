from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm, UserRegisterForm, CheckOtpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
import ghasedakpack
from django.views import View
from random import randint
from .models import Otp, User

SMS = ghasedakpack.Ghasedak("c39a4004d4c5076df9ec541aa7cfd738c84752841ae2789be435fa4823bbbec9")

# Create your views here.


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


class UserRegisterView(View):
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'Account/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            randcode = randint(1000,9999)
            cd = form.cleaned_data
            SMS.verification({'receptor': cd["phone"], 'type': '1', 'template': 'Multishop', 'param1': randcode})
            Otp.objects.create(phone=cd['phone'], code=randcode)
            print(randcode)
            return redirect(reverse('Account:check_otp') + f'?={cd["phone"]}')

        return render(request, 'Account/register.html', {'form': form})


class CheckOtpView(View):
    form_class = CheckOtpForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'Account/otp.html', {'form': form})

    def post(self, request):
        phone = request.Get.get('phone')
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], phone=phone).exists():
                user = User.objects.create_user(phone=phone)
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'Invalid code', 'danger')
                return redirect('Account:check_otp')

        return render(request, 'Account/otp.html', {'form': form})
