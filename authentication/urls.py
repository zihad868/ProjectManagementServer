from django.urls import path
from . views import CreateUserView

urlpatterns = [
    path('api/users/register', CreateUserView.as_view(), name='create-user')
]
