from django.conf.urls import url
from BlogMySelf.views import MainPageView

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name="main"),
]