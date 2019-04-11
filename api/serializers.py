# api/serializers.py

from rest_framework import serializers
from .models import Company
from .models import Version
from .models import Publication

class CompanySerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		model = Company
		fields = ('id', 'name')


class VersionSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		model = Version
		fields = ('id', 'code', 'name', 'date_created', 'date_modified', 'available')
		read_only_fields = ('date_created', 'date_modified')


class PublicationSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		model = Publication
		fields = ('id', 'date_created', 'company', 'version')
		read_only_fields = (['date_created'])