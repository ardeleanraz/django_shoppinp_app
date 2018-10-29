from django.db import models


class Employee(models.Model):
    name = models.TextField(default='')
    telephone_number = models.CharField(max_length=10)
    departament_name = models.TextField(default='')

    def __str__(self):
        return 'Nume_angajat:' + str(self.name) + ',' + 'Id_angajat:' + str(
            self.id) + ',' + 'Numar_de_telefon:' + str(
            self.telephone_number) + ',' + 'Departament:' + str(self.departament_name)


class Departament(models.Model):
    name = models.TextField(default='')
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Nume Departament:' + str(self.name) + ',' + 'id_angajat:' + str(self.id) + ',' + str(self.manager)


class Product(models.Model):
    name = models.TextField(default='')
    price = models.IntegerField(default=0)
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Nume produs:' + str(self.product) + ',' + 'Id_produs:' + str(self.id) + ',' + 'Pret:' + str(
            self.price) + ',' + str(self.departament)


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.product) + ',' + 'AN/LUNA/ZI:' + str(self.year) + '/' + str(
            self.month) + '/' + str(self.day) + ',' + str(self.employee)
