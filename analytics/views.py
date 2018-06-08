from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

from .models import UserSession

class UserSessionDetailView(DetailView):

    model = UserSession

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserSessionList(ListView):

    model = UserSession
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
