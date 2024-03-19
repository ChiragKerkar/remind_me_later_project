from django.db import models

class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=50)  # SMS or Email or other types
    created_at = models.DateTimeField(auto_now_add=True)
