from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    lecturer = models.CharField(max_length=100)
    online = models.BooleanField(default=False)
    price = models.IntegerField(default=10)

    def __str__(self):
        return self.name