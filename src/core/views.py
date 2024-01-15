from django.views.generic import TemplateView
from os import environ

class CoreView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['env'] = environ
        return context