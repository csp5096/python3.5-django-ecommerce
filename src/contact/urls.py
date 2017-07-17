# djangotemplates/catalog/urls.py

from django.conf.urls import url
from contact import views

urlpatterns = [
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
]