from django.contrib import admin
from guestbook.models import Guestbook
from goods.models import Good
from categories.models import Category


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ("posted", "user", "content")
    list_display_links = ("posted", "user")
    list_per_page = 10
    list_max_show_all = 50
    search_fields = ("user", "content")
    date_hierarchy = "posted"
    list_filter = ("user",)
    preserve_filters = False
    ordering = ("user", "posted")


class GoodAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    # readonly_fields = ("category",)
    radio_fields = {"category": admin.VERTICAL}
    save_on_top = True
    fieldsets = (
        (None, {
            "fields": (("name", "category"),)
        }),
        ("Описание", {
            "fields": ("description", "content")
        }),
        ("Цена", {
            "fields": (("price", "price_acc"),)
        }),
        ("Дополнительные параметры", {
            "classes": ("collapse",),
            "fields": (("in_stock", "featured"),)
        }),
        ("Изображение", {
            "fields": ("image",)
        })
    )


class GoodInline(admin.StackedInline):
    model = Good
    fields = (("name", "category"), "description", "content", ("price", "price_acc"), ("in_stock", "featured"), "image")


class CategoryAdmin(admin.ModelAdmin):
    fields = (("name", "order"),)
    # inlines = (GoodInline,)

admin.site.register(Guestbook, GuestbookAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Category, CategoryAdmin)
