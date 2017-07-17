# djangotemplates/catalog/urls.py

from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^catalog/$', views.CatalogPageView.as_view(), name='catalog'),
]