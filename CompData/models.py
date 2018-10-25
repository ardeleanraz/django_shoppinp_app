from django.db import models


class Employee(models.Model):
    employee_name = models.TextField(default='')
    telephone_number = models.CharField(max_length=10)
    departament_name = models.TextField(default='')


class Departament(models.Model):
    departament_name = models.TextField(default='')
    manager_name = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    product_name = models.TextField(default='')
    price = models.IntegerField(default=0)
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True)


class Sale(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
