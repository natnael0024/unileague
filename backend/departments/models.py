from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(
        "universities.University",
        on_delete=models.CASCADE,
        related_name="departments"
    )

    def __str__(self):
        return self.name
