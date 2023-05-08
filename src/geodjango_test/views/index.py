"""Index view"""
from django.views.generic import TemplateView


class Index(TemplateView):
    """Index view."""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        if "name" not in kwargs:
            kwargs["name"] = "world"
        context = super().get_context_data(**kwargs)
        return context


# Create your views here.
