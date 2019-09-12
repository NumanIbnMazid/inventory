from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/home.html")
