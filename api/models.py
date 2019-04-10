from django.db import models

# Create your models here.
class Companies(models.Model):
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