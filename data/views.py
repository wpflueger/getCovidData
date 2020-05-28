import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# from data.forms import LogMessageForm
# from data.models import LogMessage
from django.views.generic import ListView
from data.models import StateData

# REST


def home(request):
    return render(request, "data/home.html")


def about(request):
    return render(request, "data/about.html")


def contact(request):
    return render(request, "data/contact.html")


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = StateData

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
