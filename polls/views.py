from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello world, to the polls index page")
