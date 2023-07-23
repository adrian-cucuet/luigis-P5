from django.db import models


class Newsletter(models.Model):
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.full_name
