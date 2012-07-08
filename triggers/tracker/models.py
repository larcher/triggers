from django.db import models
from djangotoolbox.fields import DictField

# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=255)
    # TODO owner
    # TODO units

    def get_latest_value(self):
        # find the most recent value for this object
        # seems like the object ID may be good enough .. some of the time.  But
        # TODO should change this to use a sequence number, implemented as counter document as described here:
        # http://www.mongodb.org/display/DOCS/Object+IDs
        return DataPoint.objects.filter(thing=self).order_by('_id').reverse()[0]

    def get_previous_change(self):
        return DataPoint.objects.filter(thing=self).order_by('_id').reverse()[1]

class DataPoint(models.Model):
    datetime_stamp = models.DateTimeField(auto_now_add=True, null=True)
    value = DictField()
    dirty = models.BooleanField(default=True)
    thing = models.ForeignKey(Thing)

