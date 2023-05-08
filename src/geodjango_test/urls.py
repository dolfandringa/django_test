"""Django route config"""

from django.urls import include, path

from . import views

urlpatterns = [
    path("form", views.FormView.as_view(), name="form"),
    path("form/thanks", views.FormSuccess.as_view(), name="form_thanks"),
    path("", views.Index.as_view(), name="home"),
    path("<name>", views.Index.as_view(), name="home"),
    path("api/", include("geodjango_test.api.urls")),
]
