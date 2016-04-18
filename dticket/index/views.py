from django.shortcuts import render
from django.views.generic import FormView

from index.forms import HomePageForm

from slacker import Slacker


class HomePageView(FormView):
    template_name = "templates/index.html"
    form_class = HomePageForm
    ticket_number = 0
    success_url = '/'

    def form_valid(self, form):
        return super(HomePageView, self).form_valid(form)

    def increase_ticket_number(self):
        ticket_number += 1

    def decrease_ticket_number(self):
        ticket_number -= 1

    def slack_me(self):
        pass
