from django.shortcuts import render
from registration.models import employeedata

# Create your views here.
def home(request):
    return render(request,'home.html')

def data(request):
    username = request.POST.get('uname')
    password = request.POST.get('psw')
    emp_details = employeedata.objects.get(employee_name = username)
    return render(request,'data.html', {"emp_details":emp_details})

def registration(request):
    return render(request,'registration.html')

def upload(request):
    name = request.POST.get('name')
    #eid = request.POST.get('eid')
    email = request.POST.get('email')
    psw = request.POST.get('password')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    bdate = request.POST.get('bdate')
    gender = request.POST.get('gender')
    employe = employeedata(employee_name=name, email_id=email, password=psw, address=address, phone=phone, birth_date = bdate, gender=gender)
    employe.save()
    return render(request,'details.html', {'name':name})
    