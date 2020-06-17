
from django.conf.urls import url

from . import views


urlpatterns = [
    # 商品主页
    url(r'^index$', views.IndexView.as_view(), name='index'),
  ]
