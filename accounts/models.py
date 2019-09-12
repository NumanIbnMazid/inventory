from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from .utils import time_str_mix_slug, upload_image_path
from django.urls import reverse
from allauth.account.signals import user_logged_in, user_signed_up
from django_countries.fields import CountryField


class UserProfile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHERS = 'Others'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, related_name='profile', verbose_name='user')
    slug = models.SlugField(unique=True, verbose_name='slug')
    gender = models.CharField(choices=GENDER_CHOICES, blank=True,
                              null=True, max_length=10, verbose_name='gender')
    dob = models.DateField(blank=True, null=True, verbose_name='DOB')
    contact = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='contact')
    address = models.TextField(max_length=200, blank=True,
                               null=True, verbose_name='address')
    city = models.CharField(blank=True, null=True,
                            max_length=100, verbose_name='city')
    state = models.CharField(blank=True, null=True,
                             max_length=100, verbose_name='state/province')
    country = CountryField(blank=True, null=True)
    about = models.TextField(max_length=300, blank=True,
                             null=True, verbose_name='about')
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True, verbose_name='image')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')

    class Meta:
        verbose_name = ("User Profile")
        verbose_name_plural = ("User Profiles")
        ordering = ["-user__date_joined"]

    def get_absolute_url(self):
        return reverse("profile_details", kwargs={"slug": self.slug})

    def username(self):
        return self.user.username

    def get_username(self):
        if self.user.first_name or self.user.last_name:
            name = self.user.get_full_name()
        else:
            name = self.user.username
        return name

    def get_smallname(self):
        if self.user.first_name or self.user.last_name:
            name = self.user.get_short_name()
        else:
            name = self.user.username
        return name

    def get_dynamic_name(self):
        if len(self.get_username()) < 13:
            name = self.get_username()
        else:
            name = self.get_smallname()
        return name

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    username = instance.username.lower()
    slug_binding = username+'-'+time_str_mix_slug()
    if created:
        UserProfile.objects.create(user=instance, slug=slug_binding)
    instance.profile.save()
