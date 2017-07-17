# djangotemplates/catalog/urls.py

from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^catalog/$', views.CatalogPageView.as_view(), name='catalog'),
    url(r'^product/$', views.ProductPageView.as_view(), name='product'),
    url(r'^category/$', views.CategoryPageView.as_view(), name='category'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]