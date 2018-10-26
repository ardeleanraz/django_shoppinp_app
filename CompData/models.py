from django.db import models


class Employee(models.Model):
    employee = models.TextField(default='')
    telephone_number = models.CharField(max_length=10)
    departament_name = models.TextField(default='')

    def __str__(self):
        return 'Nume_angajat' + ':' + str(self.employee) + ',' + 'Id_angajat' + ':' + str(
            self.id) + ',' + 'Numar_de_telefon' + ':' + str(
            self.departament_name)


class Departament(models.Model):
    departament = models.TextField(default='')
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    product = models.TextField(default='')
    price = models.IntegerField(default=0)
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True)


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
