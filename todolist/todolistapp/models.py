from django.db import models

# Create your models here.
class Worklist(models.Model):
    workname = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.workname +" date = " + str(self.date)