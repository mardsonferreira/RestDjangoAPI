from django.db import models

# Create your models here.
class Company(models.Model):
	"""This class represents the Company model."""
	name = models.CharField(max_length=255, blank=False, unique=True)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "{}".format(self.name)


class Version(models.Model):
	"""This class represents the Version model."""
	name = models.CharField(max_length=255, blank=False, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	available = models.BooleanField(default=True)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "{}".format(self.name, self.available)


class Publication(models.Model):
	"""This class represents the Version model."""
	date_created = models.DateTimeField(auto_now_add=True)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	version = models.ForeignKey(Version, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a human readable representation of the model instance.""" 
		return "{}".format(self.company, self.version)		