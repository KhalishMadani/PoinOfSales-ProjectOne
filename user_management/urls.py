from django.urls import path
from .views import landing_page, sign_up

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home', landing_page, name='home'),
    path('sign-up', sign_up, name='sign_up'),
]
