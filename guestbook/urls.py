from django.conf.urls import url
from guestbook.views import GuestbookView


urlpatterns = [
    url(r'^$', GuestbookView.as_view(), name="guestbook"),
]
