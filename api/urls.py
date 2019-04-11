# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CompanyView
from .views import DetailsView
from .views import VersionView
from .views import VersionDetailsView
from .views import PublicationView
from .views import PublicationDetailsView
from .views import PublicationByDateView
from .views import PublicationByVersionCodeView

urlpatterns = {
	url(r'^companies/$', CompanyView.as_view(), name="companies"),
	url(r'^companies/(?P<pk>[0-9]+)/$',
		DetailsView.as_view(), name="companiesdetails"),
	url(r'^versions/$', VersionView.as_view(), name="versions"),
	url(r'^versions/(?P<pk>[0-9]+)/$',
		VersionDetailsView.as_view(), name="versionsdetails"),
	url(r'^publications/$', PublicationView.as_view(), name="publications"),
	url(r'^publications/(?P<pk>[0-9]+)/$',
		PublicationDetailsView.as_view(), name="publicationsdetails"),
	url(r'^publications/(?P<date>\d{4}-\d{2}-\d{2})/$',
		PublicationByDateView.as_view(), name="publicationsbydate"),
	url(r'^publications/(?P<code>[A-Z0-9_]+)/$',
		PublicationByVersionCodeView.as_view(), name="publicationsbyversioncode"),
}

urlpatterns = format_suffix_patterns(urlpatterns)