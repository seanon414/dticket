from django.db import models


class TicketCounter(models.Model):
    ticket_field = models.IntegerField()

    def __unicode__(self):
        return unicode(self.ticket_field)


class SlackMe(models.Model):
    ticket_id = models.IntegerField()
    slack_username = models.CharField(max_length=20)
