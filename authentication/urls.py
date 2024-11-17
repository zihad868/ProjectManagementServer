from django.urls import path
from . views import CreateUserView, LoginView, GetUserByIdView, UpdateUserView, DeleteUserView

urlpatterns = [
    path('api/users/register/', CreateUserView.as_view(), name='create-user'),
    path('api/users/login/', LoginView.as_view(), name='login'),
    path('api/users/<int:user_id>/', GetUserByIdView.as_view(), name='get-user-id'),
    path('api/users/<int:user_id>/update/', UpdateUserView.as_view(), name='update-user'),
    path('api/users/<int:user_id>/delete/', DeleteUserView.as_view(), name='delete-user'),
]
