from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm


def logout(request):
    return render(request, 'users/logout.html')


class SignUp(CreateView):
    form_class = CreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('posts:index')