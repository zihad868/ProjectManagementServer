from django.urls import path
from .views import ProjectListCreateView
urlpatterns = [
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list-create')
]