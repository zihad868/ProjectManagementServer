from django.db import models
from django.conf import settings
from projects.models import Projects


class Task(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ]
    
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=25, choices=PRIORITY_CHOICES, default='Medium')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title