from django.db import models

class todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(null=True)
    
    def __str__(self):
        return self.title