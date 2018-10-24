from django.db import models

class Employee(models.Model):
    name = models.TextField()
    telephone_number = models.CharField(max_length=10)
    departament_id = models.IntegerField(default=0)

class Departament(models.Model):
    name = models.TextField()
    manager_id = models.IntegerField(default=0)


class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField(default=0)
    departament_id = models.IntegerField(default=0)


class Sale(models.Model):
    product_id = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    employee_id = models.IntegerField(default=0)
