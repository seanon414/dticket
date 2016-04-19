from django.db import models


class TicketCounter(models.Model):
    ticket_field = models.IntegerField()
