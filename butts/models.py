from django.db import models

from core.models import Asset


class Butt(Asset):

	def is_smelly(self):
		print(f"Verifying 'smells' property for Butt hosted at '{self.host}' with id '{self.id}'")
		return True