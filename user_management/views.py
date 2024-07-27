from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import RegistrationForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form = RegistrationForm(form_data)
        if form.is_valid():
            print('form valid')
            user = form.save()
            return HttpResponse('successfully created')
        else:
            print(f'failed form: {form}')
    else:
        form = RegistrationForm()

    return HttpResponse('please fill all the field first')

# different method to login but achieve the same 
# def login(request):
#     form = AuthenticationForm(request, data=request.POST)
#     if form.is_valid():
#         try:
#             form.clean()
#         except ValueError:
#             print(f'error form')

#         login(request, form.get_user())
#         return HttpResponseRedirect(reverse('home'))
#     else:
#         return HttpResponse(status=401)


# class LoginUser(LoginView):
#     template_name = 'registration/login.html'