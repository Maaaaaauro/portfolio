from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=100)
    pub_date = models.DateTimeField('date published')
    img = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    task_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
        
    def __str__(self):
        return  self.title

            
