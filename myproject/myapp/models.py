from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.rollno}"

