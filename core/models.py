from django.db import models

# Painting project info is stored here
class Project(models.Model):
    name = models.CharField(max_length=50) # name of the project
    customer_name = models.CharField(max_length=50) # Customer associated to project
    description = models.TextField(blank=True) # optional description of the project
    status = models.CharField(max_length=50, default='Pending') # project status

    def __str__(self):
        return self.name

    

