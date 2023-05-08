"""Simple form."""
from django import forms
from django.urls import reverse_lazy
from django.views.generic import FormView as BaseFormView
from django.views.generic import TemplateView


class Form(forms.Form):
    """Simple form."""

    email_address = forms.EmailField()


class FormSuccess(TemplateView):
    """Success Page."""

    template_name = "form_thanks.html" ""


class FormView(BaseFormView):
    """View for the Form."""

    template_name = "form.html"
    form_class = Form
    success_url = reverse_lazy("form_thanks")
