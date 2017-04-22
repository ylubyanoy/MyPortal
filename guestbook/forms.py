from django import forms
from guestbook.models import Guestbook


class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = "__all__"
    user = forms.CharField(max_length=20, label="Пользователь")
    content = forms.CharField(widget=forms.Textarea, label="Содержимое")
    honeypot = forms.CharField(required=False, label="Ловушка для спамеров")
