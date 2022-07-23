from django.db import models


class Meal(models.Model):
	duration = models.PositiveIntegerField("Duration (ms)")
	quantity = models.PositiveSmallIntegerField("Quantity (g)")


	@property
	def duration_in_seconds(self) -> int:
		return self.duration // 1000


	def __str__(self) -> str:
		return f"{self.quantity} g eaten in {self.duration_in_seconds} s"
