from django.urls import path
from . views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path('api/tasks/<int:task_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/comments/<int:id>/', CommentDetailView.as_view(), name='comment-detail')
]
