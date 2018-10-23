
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Company index.")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
