# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CompanyView
from .views import DetailsView
from .views import VersionView
from .views import VersionDetailsView

urlpatterns = {
	url(r'^companies/$', CompanyView.as_view(), name="companies"),
	url(r'^companies/(?P<pk>[0-9]+)/$',
		DetailsView.as_view(), name="companiesdetails"),
	url(r'^versions/$', VersionView.as_view(), name="versions"),
	url(r'^versions/(?P<pk>[0-9]+)/$',
		VersionDetailsView.as_view(), name="versionsdetails"),
}

urlpatterns = format_suffix_patterns(urlpatterns)