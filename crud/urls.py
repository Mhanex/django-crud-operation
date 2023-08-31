
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create-employee/', views.createEmployee, name="create-employee"),
    path('employee-information/<int:pk>/', views.employeeInfo, name="employee-info"),
    path('update-information/<int:pk>/', views.updateEmployeeInfo, name="update-info"),
    path('delete-information/<int:pk>/', views.deleteEmployee, name="delete-info"),
]