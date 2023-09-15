from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=80)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField(null=True)
    event_description = models.CharField(max_length=255)
    lead_person = models.CharField(max_length=255, null=True)
    event_ticketed = models.BooleanField(null=False)
    event_price = models.IntegerField(null=True)
# Create your models here.
# event = Event(event_name="", event_start_date="2023-11-11 00:00", event_end_date="2023-11-11 23:59",event_description="", lead_person="Milosz", event_ticketed=False, event_price=0)