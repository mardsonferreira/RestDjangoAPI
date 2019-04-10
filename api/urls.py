# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from .views import VersionView

urlpatterns = {
	url(r'^companies/$', CreateView.as_view(), name="create"),
	url(r'^companies/(?P<pk>[0-9]+)/$',
		DetailsView.as_view(), name="details"),
	url(r'^versions/$', VersionView.as_view(), name="versions"),
}

urlpatterns = format_suffix_patterns(urlpatterns)