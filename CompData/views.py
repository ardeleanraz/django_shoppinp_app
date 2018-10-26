from django.http import HttpResponse

from CompData.models import Employee, Sale, Departament, Product

def index(request):
    total =[]
    for emp in Employee.objects.all():
        sales = Sale.objects.filter(employee=emp)
        for sale in sales:
            total.append(emp.employee_name +','+ sale.product_name)
    return HttpResponse('<br/>'.join(total))



def index1(request):
    total = []
    for dep in Departament.objects.all():
        products = Product.objects.filter(departament=dep)
        for product in products:
            total.append(dep.departament_name +','+product.product_name)

    return HttpResponse('<br/>'.join(total))