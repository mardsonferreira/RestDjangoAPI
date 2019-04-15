from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CompanySerializer
from .serializers import VersionSerializer
from .serializers import PublicationSerializer
from .models import Company
from .models import Version
from .models import Publication
from django.utils.dateparse import parse_date


class CompanyView(generics.ListCreateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

	def perform_create(self, serializer):
	    serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class VersionView(generics.ListCreateAPIView):
	queryset = Version.objects.all()
	serializer_class = VersionSerializer

	def perform_create(self, serializer):
	    serializer.save()	


class VersionDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Version.objects.all()
	serializer_class = VersionSerializer


class PublicationView(generics.ListCreateAPIView):
	queryset = Publication.objects.all()
	serializer_class = PublicationSerializer

	def perform_create(self, serializer):
	    serializer.save()

class PublicationDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Publication.objects.all()
	serializer_class = PublicationSerializer

class PublicationByDateView(generics.ListAPIView):
	serializer_class = PublicationSerializer
	lookup_url_kwarg = "date"

	def get_queryset(self):
		date_str = self.kwargs.get(self.lookup_url_kwarg)
		date =  parse_date(date_str)
		publications = Publication.objects.filter(date_created__date = date)
		return publications 	

class PublicationByVersionCodeView(generics.ListAPIView):
	serializer_class = PublicationSerializer
	lookup_url_kwarg = "code"

	def get_queryset(self):
		code = self.kwargs.get(self.lookup_url_kwarg)
		version = Version.objects.get(code = code)
		publications = Publication.objects.filter(version_id = version.id)
		return publications

class PublicationByCompanyNameView(generics.ListAPIView):
	serializer_class = PublicationSerializer
	lookup_url_kwarg = "name"

	def get_queryset(self):
		name = self.kwargs.get(self.lookup_url_kwarg)
		company = Company.objects.get(name = name)
		publications = Publication.objects.filter(company_id = company.id)
		return publications		
		
