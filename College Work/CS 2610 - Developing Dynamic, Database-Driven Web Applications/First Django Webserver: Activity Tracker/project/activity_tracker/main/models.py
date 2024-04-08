from django.db import models
from datetime import timedelta

# Create your models here.
class Activity(models.Model):
        id = models.BigAutoField(primary_key=True)
        name = models.TextField()
        
        def timeSpent(self):
                delta = timedelta()
                for timelog in self.timelog_set.all():
                        delta += (timelog.end_time - timelog.start_time)
                return str(delta)
                

class TimeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity = models.ForeignKey("Activity", on_delete = models.CASCADE) # one to many relationship
    
    def timeAmount(self):
            delta = timedelta()
            delta = self.end_time - self.start_time
            return str(delta)