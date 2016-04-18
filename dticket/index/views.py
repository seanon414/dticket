from django.shortcuts import render
from django.views.generic import TemplateView

from index.forms import HomePageForm

from slacker import Slacker


class HomePageView(TemplateView):
    template_name = "templates/index.html"
    ticket_number = 0

    def increase_ticket_number(self):
        ticket_number += 1

    def decrease_ticket_number(self):
        ticket_number -= 1

    def slack_me(self):
        pass
