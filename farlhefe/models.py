from django.db import models


class Meal(models.Model):
	duration = models.PositiveIntegerField("Duration (ms)")
	quantity = models.PositiveSmallIntegerField("Quantity (g)")


	def __str__(self) -> str:
		duration_in_seconds = self.duration // 1000
		return f"{self.quantity} g eaten in {duration_in_seconds} s"
