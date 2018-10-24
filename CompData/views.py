from django.http import HttpResponse


def index(request):
    return HttpResponse("Angajatul cu cele mai mari vanzari este:")

