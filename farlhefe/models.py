from datetime import timedelta

from django.db import models


class Meal(models.Model):
	date_created = models.DateTimeField("Date created", auto_now_add=True)
	duration = models.PositiveIntegerField("Duration (ms)")
	quantity = models.PositiveSmallIntegerField("Quantity (g)")


	@property
	def date(self):
		return self.date_created - timedelta(milliseconds=self.duration)

	@property
	def duration_in_seconds(self) -> int:
		return self.duration // 1000


	def __str__(self) -> str:
		return f"{self.quantity} g eaten in {self.duration_in_seconds} s"
