from django.db import models

class Project (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField('Description')
    language_add = models.CharField(max_length=100)
    date_loaded = models.DateTimeField(auto_now_add=True)
    img_loaded = models.ImageField(upload_to='images/', blank=False, null=True)

    def __str__(self):
        return self.title
