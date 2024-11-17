from django.db import models
from django.conf import settings
from tasks.models import Task


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Comment by {self.user} on {self.task.title}"