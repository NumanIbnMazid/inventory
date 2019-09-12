from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView,
                                  ListView, DetailView, DeleteView, TemplateView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Product
from .forms import ProductManageForm
from django.urls import reverse
from django.contrib import messages
from django import forms


@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    template_name = 'products/manage.html'
    form_class = ProductManageForm

    def form_valid(self, form):
        title = form.instance.title
        qs = Product.objects.filter(
            title__iexact=title)
        if qs.exists():
            form.add_error(
                'title', forms.ValidationError(
                    "This title is already exists!"
                )
            )
            return super().form_invalid(form)
        else:
            messages.add_message(self.request, messages.SUCCESS,
                                 "Product has been created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('products:add_product')

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView,
                        self).get_context_data(**kwargs)
        context['object_list'] = Product.objects.all().order_by('-created_at')
        context['page_title'] = 'Add Product'
        return context


@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    template_name = 'products/list.html'
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.all()
        if qs.exists():
            return qs
        return None


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    template_name = 'products/manage.html'
    form_class = ProductManageForm

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        qs = Product.objects.filter(slug=slug)
        if qs.exists():
            return qs.first()
        return None

    def form_valid(self, form):
        self.object = self.get_object()
        title = form.instance.title
        if not title == self.object.title:
            qs = Product.objects.filter(
                title__iexact=title)
            if qs.exists():
                form.add_error(
                    'title', forms.ValidationError(
                        "This title is already exists!"
                    )
                )
                return super().form_invalid(form)
        messages.add_message(self.request, messages.SUCCESS,
                             "Product has been updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('products:add_product')

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView,
                        self).get_context_data(**kwargs)
        context['object_list'] = Product.objects.all().order_by('-created_at')
        context['page_title'] = 'Add Product'
        return context


@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    template_name = 'products/manage.html'
    form_class = ProductManageForm

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        qs = Product.objects.filter(slug=slug)
        if qs.exists():
            return qs.first()
        return None

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,
                             "Product has been deleted successfully!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductDeleteView,
                        self).get_context_data(**kwargs)
        context['page_title'] = 'Delete Product'
        context['object_list'] = Product.objects.all().order_by('-created_at')
        self.object = self.get_object()
        context['destructive_msg'] = f"Are you sure you want to delete product '{self.object.title}' ?"
        return context

    def get_success_url(self):
        return reverse('products:add_product')


class ProductRestView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/rest.html")
