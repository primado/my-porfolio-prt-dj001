from django.db import models

# Create your models here.
class MLSAProgram(models.Model):
    event_title = models.CharField("Event title", max_length=200)
    event_link = models.URLField("Event Link", blank=True, null=True)
    event_description = models.CharField("Event Description", max_length=400)
    event_image = models.ImageField(blank=True, null=True)
    event_comments = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField("Time Posted", auto_now=True)
    
    def __str__(self):
        return self.event_title  
    
    class Meta:
        ordering = ("-created",)   
    
class Project(models.Model):
    project_name = models.CharField(max_length=60)
    project_description = models.CharField(max_length=400)
    created = models.DateTimeField("Time Created", auto_now=True)
    project_image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.project_name
    