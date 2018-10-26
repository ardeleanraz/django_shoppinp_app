from django.urls import path

from . import views

urlpatterns = [
    path('employee/', views.index, name='index'),
    path('product/',views.index1, name='index1')
]