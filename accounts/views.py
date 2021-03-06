from django.shortcuts import render
from django.views.generic import UpdateView, DetailView, ListView
from .models import UserProfile
from .forms import UserProfileUpdateForm
from django import forms
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self):
        qs = UserProfile.objects.filter(slug=self.kwargs['slug'])
        if qs.exists():
            return qs.first()
        return None


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    template_name = 'profile/profile-update.html'
    form_class = UserProfileUpdateForm

    def get_object(self):
        qs = UserProfile.objects.filter(slug=self.kwargs['slug'])
        if qs.exists():
            return qs.first()
        return None

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,
                             "Your profile has been updated successfully !")
        return super().form_valid(form)

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse('profile_details', kwargs={'slug': slug})
