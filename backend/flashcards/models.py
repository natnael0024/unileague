from django.db import models
from django.conf import settings

class Flashcard(models.Model):
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="flashcards"
    )
    front = models.TextField()
    back = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.front[:50]



class FlashcardReview(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="flashcard_reviews"
    )
    flashcard = models.ForeignKey(
        Flashcard,
        on_delete=models.CASCADE
    )
    knew_it = models.BooleanField()
    reviewed_at = models.DateTimeField(auto_now_add=True)