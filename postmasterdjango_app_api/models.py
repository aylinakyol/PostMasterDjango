from django.db import models # type: ignore

class Task(models.Model):
    description = models.TextField(null=False, blank=False)
    is_completed = models.BooleanField(null=False, blank=False, default=False)
    due_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.description