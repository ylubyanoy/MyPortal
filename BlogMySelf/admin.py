from django.contrib import admin
from guestbook.models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ("posted", "user", "content")
    list_display_links = ("posted", "user")
    list_per_page = 10
    list_max_show_all = 50

admin.site.register(Guestbook, GuestbookAdmin)
