from django.db import models
from djangotoolbox.fields import DictField

# Create your models here.


class TrackedObject(models.Model):
    name = models.CharField(max_length=255)
    # TODO owner
    # TODO units

    def get_latest_value(self):
        # find the most recent value for this object
        return ObjectValue.objects.filter(tracked_object=self).order_by('datetime_stamp').reverse()[0]

    def get_previous_change(self):
        return ObjectValue.objects.filter(tracked_object=self).order_by('datetime_stamp').reverse()[1]

class ObjectValue(models.Model):
    datetime_stamp = models.DateTimeField(auto_now_add=True, null=True)
    value = DictField()
    dirty = models.BooleanField(default=True)
    tracked_object = models.ForeignKey(TrackedObject)

