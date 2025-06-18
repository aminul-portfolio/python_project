from django.db import models

# models.py
class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    page_name = models.CharField(max_length=100)  # Track which page this comment is for

    def __str__(self):
        return f"{self.text[:30]}..."
