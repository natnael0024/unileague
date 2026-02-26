from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
