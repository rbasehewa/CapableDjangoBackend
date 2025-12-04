from django.db import models

class Todo(models.Model):
    # Short text describing the task
    title = models.CharField(max_length=255)

    # Whether the task is finished or not
    completed = models.BooleanField(default=False)

    # When the todo was created – auto-filled by Django
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        # This is what you’ll see in the admin / shell
        return self.title
