from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)  # optional field
    enrolled_date = models.DateField(auto_now_add=True)       # automatically sets date

    def __str__(self):
        return self.name
