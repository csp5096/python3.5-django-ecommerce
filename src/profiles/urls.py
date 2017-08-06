from django.conf.urls import url
from profiles import views

urlpatterns = [
    url ( r'^profile/$', login_required ( TemplateView.as_view ( template_name="profile.html" ) ) )
]