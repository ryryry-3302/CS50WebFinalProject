from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    
    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=400)
    poster = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True)
    
    def __str__(self):
        return f"{self.poster}'s task {self.title}"
    create_time = models.DateTimeField(default=timezone.now, blank=True, editable=False)
    modified = models.DateTimeField(blank= True, default=timezone.now)

    def save(self, *args, **kwargs):
        self.modified =timezone.now()
        return super(Task, self).save(*args, **kwargs)