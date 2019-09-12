from django.urls import path, include
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/<slug>/view/',
         ProfileDetailView.as_view(), name='profile_details'),
    path('profile/<slug>/update/',
         ProfileUpdateView.as_view(), name='profile_update'),
]
