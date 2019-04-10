# api/serializers.py

from rest_framework import serializers
from .models import Companies

class CompaniesSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		model = Companies
		fields = ('id', 'name')
