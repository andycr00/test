from django.db import models

class Client(models.Model):
    document = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, editable=False
    )
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
