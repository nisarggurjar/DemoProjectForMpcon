from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=128, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name