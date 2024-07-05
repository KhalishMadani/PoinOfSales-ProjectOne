from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import RegistrationForm

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def sign_up(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form = RegistrationForm(form_data)
        if form.is_valid():
            print('form valid')
            user = form.save()
            login(request, user)
            return redirect('/home')
        else:
            print(f'failed form: {form}')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})