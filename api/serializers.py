# api/serializers.py

from rest_framework import serializers
from .models import Companies
from .models import Version

class CompaniesSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		model = Companies
		fields = ('id', 'name')


class VersionSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		model = Version
		fields = ('id', 'name', 'date_created', 'date_modified', 'available')
		read_only_fields = ('date_created', 'date_modified')		
