from django.shortcuts import render, render_to_response
from django.views.generic import FormView

from index.forms import HomePageForm

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
            if 'button_slack' in form.data:
                self.slack_me()
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def slack_me(self):
        slack.chat.post_message('#d-ticket-hack', 'Hello! We will notify you when your ticket is called.')
