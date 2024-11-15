from django.urls import path
from . views import CreateUserView, LoginView

urlpatterns = [
    path('api/users/register', CreateUserView.as_view(), name='create-user'),
    path('api/users/login', LoginView.as_view(), name='login')
]
