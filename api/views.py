from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CompaniesSerializer
from .models import Companies


class CreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api."""
	queryset = Companies.objects.all()
	serializer_class = CompaniesSerializer

	def perform_create(self, serializer):
	    """Save the post data when creating a new company."""
	    serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""

	queryset = Companies.objects.all()
	serializer_class = CompaniesSerializer