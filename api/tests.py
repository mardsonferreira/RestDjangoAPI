from django.test import TestCase

# Create your tests here.
from .models import Company
from .models import Version
from .models import Publication
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelCompanyTestcase(TestCase):
	"""This class defines the test suite for the companies model."""

	def setUp(self):
		self.company_name = "Polibras"
		self.company = Company(name = self.company_name)


	def test_model_can_create_a_company(self):
		"""Test the company model can create a company."""
		old_count = Company.objects.count()
		self.company.save()
		new_count = Company.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewCompanyTestCase(TestCase):
	"""Test suite for the api views."""

	def setUp(self):
	    """Define the test client and other test variables."""
	    self.client = APIClient()
	    self.company_data = {'name': 'Polibras'}
	    self.response = self.client.post(
	        reverse('companies'),
	        self.company_data,
        format="json")

	def test_api_can_create_a_company(self):
		"""Test the api has company creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_get_a_company(self):
		"""Test the api can get a given company."""
		company = Company.objects.get()
		response = self.client.get(reverse('companiesdetails', kwargs={'pk': company.id}),format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, company)

	def test_api_can_update_company(self):
		"""Test the api can update a given company."""
		company = Company.objects.get()
		change_company = {'name': 'Something new'}
		res = self.client.put(reverse('companiesdetails', kwargs={'pk': company.id}),
			change_company, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def test_api_can_delete_company(self):
	    """Test the api can delete a company."""
	    company = Company.objects.get()
	    response = self.client.delete(
	        reverse('companiesdetails', kwargs={'pk': company.id}),
	        format='json',
	        follow=True)

	    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)		

class VersionModelTestcase(TestCase):
	"""This class defines the test suite for the version model."""

	def setUp(self):
		self.version_name = "V1.1"
		self.version = Version(name = self.version_name)


	def test_model_can_create_a_version(self):
		"""Test the version model can create a version."""
		old_count = Version.objects.count()
		self.version.save()
		new_count = Version.objects.count()
		self.assertNotEqual(old_count, new_count)


class ViewVersionTestCase(TestCase):
	"""Test suite for the api views."""

	def setUp(self):
	    """Define the test client and other test variables."""
	    self.client = APIClient()
	    self.version_data = {'name': 'V1.1', 'code' : 'WEB2900'}
	    self.response = self.client.post(
	        reverse('versions'),
	        self.version_data,
        format="json")

	def test_api_can_create_a_version(self):
		"""Test the api has version creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_get_a_version(self):
		"""Test the api can get a given version."""
		version = Version.objects.get()
		response = self.client.get(reverse('versionsdetails', kwargs={'pk': version.id}),format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, version)

	def test_api_can_update_version(self):
		"""Test the api can update a given version."""
		version = Version.objects.get()
		change_version = {'name': 'Something new', 'code' : 'DESK11'}
		res = self.client.put(reverse('versionsdetails', kwargs={'pk': version.id}),
			change_version, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def test_api_can_delete_version(self):
	    """Test the api can delete a version."""
	    version = Version.objects.get()
	    response = self.client.delete(
	        reverse('versionsdetails', kwargs={'pk': version.id}),
	        format='json',
	        follow=True)

	    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)		


class ModelPublicationTestcase(TestCase):
	"""This class defines the test suite for the publication model."""

	def setUp(self):
		self.version = Version(id= 1, name = "name", code = "WEB2019")
		self.company = Company(id=1, name = "name")
		self.publication = Publication(version = self.version, company = self.company)


	def test_model_can_create_a_publication(self):
		"""Test the publication model can create a version."""
		old_count = Publication.objects.count()
		self.version.save()
		self.company.save()
		self.publication.save()
		new_count = Publication.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewPublicationTestCase(TestCase):
	"""Test suite for the api views."""

	def setUp(self):
		"""Define the test client and other test variables."""
		version = Version.objects.create(name="Initial", code= "DESK11")
		company = Company.objects.create(name="mycompany")
		self.client = APIClient()
		self.publication_data = {"company": company.id , "version": version.id}
		self.response = self.client.post(
			reverse('publications'),
			self.publication_data,
			format="json")

	def test_api_can_create_a_publication(self):
		"""Test the api has publication creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


	def test_api_can_get_a_publication(self):
		"""Test the api can get a given version."""
		new_client = APIClient()
		response = new_client.get('/publications/', kwargs={'pk': 1}, format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_api_can_get_a_publication_by_date(self):
		new_client = APIClient()
		response = new_client.get('/publications/', kwargs={'pk': '2019-04-11'}, format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)	

	def test_api_can_get_a_publication_by_version(self):
		new_client = APIClient()
		response = new_client.get('/publications/', kwargs={'pk': 'CODE11'}, format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)		

	def test_api_can_get_a_publication_by_company(self):
		new_client = APIClient()
		response = new_client.get('/publications/', kwargs={'pk': 'COMPANY'}, format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)			
