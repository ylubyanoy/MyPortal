from django.db import models


class Guestbook(models.Model):
    user = models.CharField(max_length=20, verbose_name="Пользователь")
    posted = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    content = models.TextField(verbose_name="Содержимое")

    def get_formatted_datetime(self):
        return str(self.posted.day) + "." + str(self.posted.month) + "." + str(self.posted.year) + " " + \
               str(self.posted.hour) + ":" + str(self.posted.minute) + ":" + str(self.posted.second)

    get_formatted_datetime.short_description = "Опубликовано"

    class Meta:
        ordering = ["-posted"]
        verbose_name = "запись гостевой книги"
        verbose_name_plural = "записи гостевой книги"
