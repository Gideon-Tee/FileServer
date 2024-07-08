from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
    emails_sent = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.title}'
