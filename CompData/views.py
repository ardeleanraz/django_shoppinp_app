from django.http import HttpResponse




def index(request):
    from CompData.models import Employee
    for emp in Employee.objects.all():
        print(emp.employee_name)
        return HttpResponse("Numele angajatului:" )

