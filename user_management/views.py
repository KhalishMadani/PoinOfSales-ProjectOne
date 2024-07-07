from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistrationForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form = RegistrationForm(form_data)
        if form.is_valid():
            print('form valid')
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            print(f'failed form: {form}')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})

# different method to login but achieve the same 
def login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        try:
            form.clean()
        except ValueError:
            print(f'error form')

        login(request, form.get_user())


class LoginUser(LoginView):
    template_name = 'registration/login.html'