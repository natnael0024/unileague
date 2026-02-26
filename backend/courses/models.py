from django.db import models

class Course(models.Model):
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="courses"
    )
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("department", "name", "year")

    def __str__(self):
        return f"{self.name} (Year {self.year})"
