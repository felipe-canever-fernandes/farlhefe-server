from statistics import quantiles
from django.test import TestCase

from .models import Meal


class MealModelTests(TestCase):
	def test_str(self):
		meal = Meal(duration=5000, quantity=500)
		self.assertEqual(str(meal), "500 g eaten in 5 s")

		meal.duration = 15500
		meal.quantity = 1500
		self.assertEqual(str(meal), "1500 g eaten in 15 s")
