from django.shortcuts import render, render_to_response
from django.views.generic import FormView

from index.forms import HomePageForm
from db.models import TicketCounter, SlackMe

from slacker import Slacker

slack = Slacker('xoxb-35700221924-XjG9qR4swYgOf4uEIWy1F7JG')


class HomePageView(FormView):
    template_name = "templates/index.html"
    form_class = HomePageForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            slack_username = form.cleaned_data['slack_username']
            ticket_id = form.cleaned_data['ticket_id']
            ticket_number = form.cleaned_data['ticket_number']
            self.save_ticket_number(ticket_number)
            if 'button_slack' in form.data:
                self.slack_initial_message(slack_username, ticket_id)
                self.save_slack_me(slack_username, ticket_id)
            elif 'button_next' in form.data:
                self.slack_ticket_called(ticket_number)
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def get_initial(self):
        initial = super(HomePageView, self).get_initial()
        initial['ticket_number'] = TicketCounter.objects.first().ticket_field
        return initial

    def save_ticket_number(self, ticket_number):
        ticket_counter = TicketCounter.objects.get(id=1)
        ticket_counter.ticket_field = ticket_number
        ticket_counter.save()

    def slack_initial_message(self, user_name, ticket_id):
        slack_string = 'Hello @{}! We will notify you when your ticket, {}, is called.'.format(user_name, ticket_id)
        slack.chat.post_message('#d-ticket-hack', slack_string)

    def slack_ticket_called(self, ticket_id):
        slack_me = SlackMe.objects.get(ticket_id=ticket_id)
        slack_string = '@{}! Your ticket, {}, has been called.'.format(user_name, ticket_id)
        slack.chat.post_message('#d-ticket-hack', slack_string)

    def save_slack_me(self, user_name, ticket_id):
        slack_me = SlackMe.objects.create(slack_username=user_name, ticket_id=ticket_id)
        slack_me.save()
