from generic.mixins import CategoryListMixin
from django.views.generic.base import TemplateView


class MainPageView(TemplateView, CategoryListMixin):
    template_name = "mainpage.html"
