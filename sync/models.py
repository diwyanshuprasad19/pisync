from django.db import models

class SyncEvent(models.Model):
    device_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    total_files_synced = models.IntegerField()
    total_errors = models.IntegerField()
    internet_speed = models.FloatField()

    def __str__(self):
        return f"{self.device_id} @ {self.timestamp}"
