from django.conf.urls import url
from django.contrib.auth.decorators import permission_required
from goods.views import GoodsListView, GoodDetailView, GoodCreate, GoodUpdate, GoodDelete


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', GoodsListView.as_view(), name="goods_index"),
    url(r'^(?P<pk>\d+)/detail/$', GoodDetailView.as_view(), name="goods_detail"),
    url(r'^(?P<pk>\d+)/add/$', permission_required("goods.add_good")(GoodCreate.as_view()), name="goods_add"),
    url(r'^(?P<pk>\d+)/edit/$', permission_required("goods.change_good")(GoodUpdate.as_view()), name="goods_edit"),
    url(r'^(?P<pk>\d+)/delete/$', permission_required("goods.delete_good")(GoodDelete.as_view()), name="goods_delete"),
]
