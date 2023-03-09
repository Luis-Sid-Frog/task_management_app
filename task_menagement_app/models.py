from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.first_name


class Task(models.Model):
    TASK_STATUS = (
        ('Nowy','Nowe zadanie'),
        ('W toku', 'W trakcie realizacji'),
        ('Rozwiązany', 'Zadanie rozwiązane')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=TASK_STATUS, max_length=32, default='Nowy'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_request_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title

