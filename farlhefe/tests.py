from django.test import TestCase

from .models import Meal


class MealModelTests(TestCase):
	def test_duration_in_seconds(self):
		meal = Meal(duration=5000, quantity=500)
		self.assertEqual(meal.duration_in_seconds, 5)

		meal.duration = 15500
		self.assertEqual(meal.duration_in_seconds, 15)


	def test_str(self):
		meal = Meal(duration=5000, quantity=500)
		self.assertEqual(str(meal), "500 g eaten in 5 s")
