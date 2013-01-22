from django.db import models

class MailingList(models.Model):
    email_address = models.CharField(max_length=500)


class Event(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    description = models.TextField()

    location = models.TextField()
    location_map_url = models.URLField()

    class Meta:
        ordering = ['datetime']

    
    def __unicode__(self):
        return u'%s' % self.pk

    def short_description(self):
        if len(self.description) > 2000:
            return self.description[0:2000] + "..."
        else:
            return self.description
