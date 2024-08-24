from django.urls import path
from .views import sign_up, LoginUser

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('home', LoginUser.as_view(), name='login_user'),
]
