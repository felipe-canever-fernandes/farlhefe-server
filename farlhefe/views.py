from django.http import HttpResponse


def index(request):
	del request
	return HttpResponse("Hello, Farlhefe!")
