from django.db import models

DEPARTMENT_CHOICES = [
        ('General Info', 'General Info'),
        ('Events', 'Events'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other'),
    ]


class ContactUs(models.Model):
    """ Model for contact form """

    class Meta:
        verbose_name_plural = 'Contact Us'

    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES,
                                  default='General Info', null=False,
                                  blank=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
