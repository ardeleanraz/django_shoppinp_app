"""Company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from CompData.views import index1, index, print_employee, print_departament, print_product, print_sale, max_words, \
    product_max_price, best_sale, best_employee

urlpatterns = [
    path('departament_product/', index1, name='departament_product/'),
    path('admin/', admin.site.urls),
    path('employee_sale/', index, name='employee_sale/'),
    path('employee_list/', print_employee, name='employee_list/'),
    path('departament_list/', print_departament, name='print_departament/'),
    path('product_list/', print_product, name='product_list/'),
    path('sale_list/', print_sale, name='sale_list/'),
    path('max_words/', max_words, name='max_words/'),
    path('product_max_price/', product_max_price, name='product__max_price/'),
    path('best_sale/', best_sale, name='best_sale/'),
    path('best_employee/',best_employee, name='best_employee'),

]
