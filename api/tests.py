from django.test import TestCase

# Create your tests here.
from .models import Companies
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestcase(TestCase):
	"""This class defines the test suite for the companies model."""

	def setUp(self):
		self.companies_name = "Polibras"
		self.companies = Companies(name = self.companies_name)


	def test_model_can_create_a_company(self):
		"""Test the company model can create a company."""
		old_count = Companies.objects.count()
		self.companies.save()
		new_count = Companies.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
	"""Test suite for the api views."""

	def setUp(self):
	    """Define the test client and other test variables."""
	    self.client = APIClient()
	    self.companies_data = {'name': 'Polibras'}
	    self.response = self.client.post(
	        reverse('create'),
	        self.companies_data,
        format="json")

	def test_api_can_create_a_company(self):
		"""Test the api has company creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


	def test_api_can_update_companies(self):
		"""Test the api can update a given company."""
		companies = Companies.objects.get()
		change_companies = {'name': 'Something new'}
		res = self.client.put(reverse('details', kwargs={'pk': companies.id}),
			change_companies, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def test_api_can_delete_companies(self):
	    """Test the api can delete a bucketlist."""
	    companies = Companies.objects.get()
	    response = self.client.delete(
	        reverse('details', kwargs={'pk': companies.id}),
	        format='json',
	        follow=True)

	    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)		

	def test_api_can_get_a_company(self):
		"""Test the api can get a given company."""
		companies = Companies.objects.get()
		response = self.client.get(reverse('details', kwargs={'pk': companies.id}),format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		#self.assertContains(response, companies)

