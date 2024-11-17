from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from tasks.models import Task
from .models import Comment
from .serializers import CommentSerializer, CommentCreateUpdateSerializer
 
class CommentListCreateView(APIView):
     
     def get(self, request, task_id, *args, **kwargs):
         task = get_object_or_404(Task, id=task_id)
         comments = task.comments.all()
         serializer = CommentSerializer(comments, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)