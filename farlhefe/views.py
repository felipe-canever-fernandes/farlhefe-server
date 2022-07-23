from django.shortcuts import render

from .models import Meal


def index(request):
	return render(request, "farlhefe/index.html", {
		"meals": Meal.objects.all()
	})
