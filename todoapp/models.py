from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)  # New remarks field

    def __str__(self):
        return self.title
