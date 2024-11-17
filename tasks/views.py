from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from . models import Task
from projects.models import Projects
from . serializers import TaskSerializer, TaskCrateSerializer


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request, project_id, *args, **kwargs):
        project = get_object_or_404(Projects, id=project_id)
        tasks = project.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, project_id, *args, **kwargs):
        project = get_object_or_404(Projects, id=project_id)
        serializer = TaskCrateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
