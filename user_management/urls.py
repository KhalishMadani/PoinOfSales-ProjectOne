from django.urls import path
from .views import sign_up, LoginUser, login

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    
    path('login/', LoginUser.as_view(), name='login_user')
]
