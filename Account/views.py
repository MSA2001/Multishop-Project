from django.shortcuts import render
from .forms import UserLoginForm

# Create your views here.
from django.views import View


class UserLoginView(View):
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'Account/login.html', {'form': form})

