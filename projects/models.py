from django.db import models
from django.conf import settings
from random import choices

class Projects(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_project')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class ProjectMembers(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member')
    ]
    project = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_membership')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f'{self.user.email} - {self.project.name} - ({self.role})'