from django import forms
from .models import Product
from django.template.defaultfilters import filesizeformat
from django.conf import settings


class ProductManageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductManageForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = "Only '_A-z0-9+-.,' these characters and spaces are allowed."
        self.fields['title'].widget.attrs.update({
            'id': 'product_title_input',
            'placeholder': 'Enter product title...',
            'maxlength': 50,
            'pattern': "^[_A-z0-9 +-.,]{1,}$"
        })
        self.fields['image'].help_text = "Select Product Image."
        self.fields['image'].widget.attrs.update({
            'id': 'product_image_input',
            'placeholder': 'Select product image...',
        })
        self.fields['quantity'].help_text = "Only numeric values allowed."
        self.fields['quantity'].widget.attrs.update({
            'id': 'product_quantity_input',
            'placeholder': 'Enter product quantity...',
            'maxlength': 50,
            'pattern': "^[0-9]{1,}$"
        })
        self.fields['price'].help_text = "Only decimal values allowed."
        self.fields['price'].widget.attrs.update({
            'id': 'product_price_input',
            'placeholder': 'Enter product price...',
            'maxlength': 50,
            'pattern': "^[0-9.]{1,}$"
        })
        self.fields['description'].help_text = "Maximum 1000 characters allowed."
        self.fields['description'].widget.attrs.update({
            'id': 'product_description_input',
            'placeholder': 'Enter product description...',
            'maxlength': 1000,
            'rows': 2,
            'cols': 2,
        })

    class Meta:
        model = Product
        fields = ['title', 'image', 'quantity',
                  'price', 'description']
        exclude = ['slug', 'created_at', 'updated_at']
