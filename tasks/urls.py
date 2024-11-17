from django.urls import path
from . views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('api/projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
]
