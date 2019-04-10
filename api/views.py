from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CompanySerializer
from .serializers import VersionSerializer
from .serializers import PublicationSerializer
from .models import Company
from .models import Version
from .models import Publication



class CompanyView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api."""
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

	def perform_create(self, serializer):
	    """Save the post data when creating a new company."""
	    serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""

	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class VersionView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api."""
	queryset = Version.objects.all()
	serializer_class = VersionSerializer

	def perform_create(self, serializer):
	    """Save the post data when creating a new company."""
	    serializer.save()	


class VersionDetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""

	queryset = Version.objects.all()
	serializer_class = VersionSerializer


class PublicationView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api."""
	queryset = Publication.objects.all()
	serializer_class = PublicationSerializer

	def perform_create(self, serializer):
	    """Save the post data when creating a new company."""
	    serializer.save()

class PublicationDetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""

	queryset = Publication.objects.all()
	serializer_class = PublicationSerializer
