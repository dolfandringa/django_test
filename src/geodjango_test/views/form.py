"""Simple form."""
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, ValidationError
from django.urls import reverse_lazy
from django.views.generic import FormView as BaseFormView
from django.views.generic import TemplateView


class Form(forms.Form):
    """Simple form."""

    email_address = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def login(self):
        """Log the user in."""
        user_model = get_user_model()
        email_address = self.cleaned_data["email_address"]
        password = self.cleaned_data["password"]
        try:
            user = user_model.objects.get(email=email_address)
        except ObjectDoesNotExist as exc:
            raise PermissionDenied("Email or password invalid.") from exc
        if not user or not user.check_password(password):
            raise PermissionDenied("Email or password invalid")


class FormSuccess(TemplateView):
    """Success Page."""

    template_name = "form_thanks.html"


class FormView(BaseFormView):
    """View for the Form."""

    template_name = "form.html"
    form_class = Form
    success_url = reverse_lazy("form_thanks")

    def form_valid(self, form: Form):
        try:
            form.login()
            return super().form_valid(form)
        except PermissionDenied:
            form.add_error(None, ValidationError("Invalid email or password"))
            return super().form_invalid(form)
