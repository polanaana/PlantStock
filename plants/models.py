from django.db import models

class Plant_name(models.Model):
    """Plant name added by user."""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.text
