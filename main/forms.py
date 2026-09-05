from django import forms

from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            "name",
            "business_name",
            "email",
            "phone",
            "business_type",
            "website_requirement",
            "message",
        ]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Your full name", "autocomplete": "name",
            }),
            "business_name": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Your business name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control", "placeholder": "you@business.com", "autocomplete": "email",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Phone or WhatsApp number",
            }),
            "business_type": forms.Select(attrs={"class": "form-control"}),
            "website_requirement": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={
                "class": "form-control", "placeholder": "Tell WebOra a little about your business and what you need.",
                "rows": 5,
            }),
        }
        labels = {
            "business_name": "Business Name",
            "phone": "Phone / WhatsApp",
            "business_type": "Business Type",
            "website_requirement": "Website Requirement",
        }
