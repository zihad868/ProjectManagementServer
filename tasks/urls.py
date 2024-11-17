from django.urls import path
from . views import TaskListCreateView

urlpatterns = [
    path('api/projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
]
