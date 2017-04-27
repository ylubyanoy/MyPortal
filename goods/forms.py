from django.forms import ModelForm
from goods.models import Good


class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = "__all__"
