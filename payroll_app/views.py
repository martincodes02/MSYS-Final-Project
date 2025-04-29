from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return render(request, 'payroll_app/trial.html')

def create_employee(request):
    return render(request, 'payroll_app/create_employee.html')

def update_employee(request):
    return render(request, 'payroll_app/update_employee.html')