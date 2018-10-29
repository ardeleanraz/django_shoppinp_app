from django.urls import path

from . import views

urlpatterns = [
    path('employee_sale/', views.index, name='index'),
    path('departament_product/', views.index1, name='index1'),
    path('employee_list/', views.print_employee, name='print_employee'),
    path('departament_list/', views.print_departament, name='print_departament'),
    path('product_list/', views.print_product, name='product_list/'),
    path('sale_list/', views.print_sale, name='sale_list/'),
    ]
