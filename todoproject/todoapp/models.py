from django.db import models
class ToDo(models.Model):
    name=models.TextField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.name

# Create your models here.
