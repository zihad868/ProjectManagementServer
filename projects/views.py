from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . models import Projects
from . serializers import ProjectSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


# Project Start
class ProjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, *args, **kwargs):
        # Retrieve a specific project by ID
        project = get_object_or_404(Projects, id=id, owner=request.user)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        # Fully update a specific project
        project = get_object_or_404(Projects, id=id, owner=request.user)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, *args, **kwargs):
        # Partially update a specific project
        project = get_object_or_404(Projects, id=id, owner=request.user)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        # Delete a specific project
        project = get_object_or_404(Projects, id=id, owner=request.user)
        project.delete()
        return Response({"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# Project End


