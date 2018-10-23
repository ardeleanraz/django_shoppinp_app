from django.db import models

class Employee(models.Model):
    name = models.TextField
    telephone_number = models.IntegerField
    departamen_id = models.IntegerField

class Departament(models.Model):
    name = models.TextField
    manager_id = models.IntegerField


class Product(models.Model):
    name = models.TextField
    price = models.IntegerField
    departament_id = models.IntegerField


class Sale(models.Model):
    product_id = models.IntegerField
    year = models.IntegerField
    month = models.IntegerField
    day = models.IntegerField
    employee_id = models.IntegerField
