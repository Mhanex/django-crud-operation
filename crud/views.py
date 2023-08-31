from django.shortcuts import render, redirect


# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from crud.forms import CreateEmployeeForm, UpdateEmployeeForm
from crud.models import Employee


def index(request):
    
    return render(request, 'crud/index.html')





@login_required(login_url='signin')
def createEmployee(request):
    employeeForm = CreateEmployeeForm()

    if request.method == "POST":
        employeeForm = CreateEmployeeForm(request.POST)

        if employeeForm.is_valid():
            employee = employeeForm.save(commit=False)
            employee.created_by = request.user
            employee.save()
            messages.success(request, f"Employee Successfully Created")
            return redirect("dashboard")
        else:
            print("All Employes Details")
    else:
        print("All fields are required")

    context= {'employeeForm': employeeForm}
    return render(request, 'crud/create-employee.html', context)




@login_required(login_url='signin')
def employeeInfo(request, pk):
    viewEmployee = Employee.objects.get(id=pk)

    context = {'viewEmployee': viewEmployee}
    return render(request, 'crud/view-employee.html', context)




@login_required(login_url='signin')
def updateEmployeeInfo(request, pk):
    fetchEmployee = Employee.objects.get(id=pk)
    updateForm = UpdateEmployeeForm(instance=fetchEmployee)
    
    if request.method == "POST":
        updateForm = UpdateEmployeeForm(request.POST, instance=fetchEmployee)

        if updateForm.is_valid():
           employee_updated_by = updateForm.save(commit=False)
           employee_updated_by.created_by = request.user
           employee_updated_by.save()

           messages.success(request, f"Record Updated Successfully")
           return redirect("dashboard")


    context = {'updateForm': updateForm}
    return render(request, 'crud/update-employee.html', context)

@login_required(login_url='signin')
def deleteEmployee(request, pk):
    fetchEmployee = Employee.objects.get(id=pk)

    fetchEmployee.delete()

    messages.success(request, f"Record for {fetchEmployee.first_name}  {fetchEmployee.last_name} deleted sucessfully")

    return redirect("index")