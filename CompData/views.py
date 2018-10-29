from django.http import HttpResponse

from CompData.models import Employee, Sale, Departament, Product


def index(request):
    total = []
    for emp in Employee.objects.all():
        sales = Sale.objects.filter(employee=emp)
        for sale in sales:
            total.append(
                'Nume angajat:' + emp.name + ',' + 'Nume produs:' + str(sale.product.name) + ',' + 'Pret Produs:' + str(
                    sale.product.price))
    return HttpResponse('<br/>'.join(total))


def index1(request):
    total = []
    for dep in Departament.objects.all():
        products = Product.objects.filter(departament=dep)
        for product in products:
            total.append('Departament:' + dep.name + ',' + 'Departament_product:' + product.name)

    return HttpResponse('<br/>'.join(total))


def print_employee(request):
    total = []
    for emp in Employee.objects.all():
        total.append('Nume angajat:' + emp.name + ',' + 'Numar de telefon:' + str(
            emp.telephone_number) + ',' + 'Departament:' + emp.departament_name)

    return HttpResponse('<br/>'.join(total))


def print_departament(request):
    total = []
    for dep in Departament.objects.all():
        total.append('Nume departament:' + dep.name + ',' + str(dep.manager))

    return HttpResponse('<br>/'.join(total))


def print_product(request):
    total = []
    for product in Product.objects.all():
        total.append(
            'Id:' + str(product.id) + ',' + 'Nume Produs:' + product.name + ',' + 'Pret Produs:' + str(
                product.price) + ',' + 'Departament:' + str(product.departament.name))

    return HttpResponse('<br>/'.join(total))


def print_sale(request):
    total = []
    for sale in Sale.objects.all():
        total.append('Id:' + str(
            sale.id) + ',' + 'Nume produs:' + sale.product.name + ',' + 'Year/month/day:' + str(sale.year) + '/' + str(
            sale.month) + '/' + str(sale.day) + ',' + 'Vanzator:' + sale.employee.name + ',' + 'Pret Produs:' + str(sale.product.price))

    return HttpResponse('<br/>'.join(total))
