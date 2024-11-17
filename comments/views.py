from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from .models import Comment
from .serializers import CommentSerializer, CommentCreateUpdateSerializer
 
class CommentListCreateView(APIView):
     
     permission_classes = [IsAuthenticated]
     
     def get(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, id=task_id)
        comments = task.comments.all()  # Related name 'comments'
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
     def post(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, id=task_id)
        serializer = CommentCreateUpdateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user, task=task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CommentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, *args, **kwargs):
        # Retrieve details of a specific comment
        comment = get_object_or_404(Comment, id=id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        # Update a specific comment (full update)
        comment = get_object_or_404(Comment, id=id, user=request.user)
        serializer = CommentCreateUpdateSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, *args, **kwargs):
        # Partially update a specific comment
        comment = get_object_or_404(Comment, id=id, user=request.user)
        serializer = CommentCreateUpdateSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        # Delete a specific comment
        comment = get_object_or_404(Comment, id=id, user=request.user)
        comment.delete()
        return Response({'message': 'Comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)