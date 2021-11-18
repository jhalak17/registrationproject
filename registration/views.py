from django.shortcuts import render, redirect
from registration.models import employeedata
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def data(request):
    try:
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        #emp_det = auth.authenticate(username=username, password=password)
        emp_details = employeedata.objects.get(employee_name = username)
        #print(emp_details)
        if password == emp_details.password:
            return render(request,'data.html', {"emp_details":emp_details})
        else:
            messages.error(request, " Invalid password")
            return redirect('home')
    except Exception as e:
        return HttpResponse(e)


def registration(request):
    return render(request,'registration.html')

def upload(request):
    name = request.POST.get('name')
    #eid = request.POST.get('eid')
    email = request.POST.get('email')
    psw = request.POST.get('password')
    c_psw = request.POST.get('c_password')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    bdate = request.POST.get('bdate')
    gender = request.POST.get('gender')
    
    if psw != c_psw:
        messages.error(request, "Password should match Confirm password")
        return redirect('registration')
    else:
        try:
            emp_details = employeedata.objects.get(employee_name = name)
            messages.error(request, " Employee Name already exist ")
            return redirect('registration')
        except:
            employe = employeedata(employee_name=name, email_id=email, password=psw, address=address, phone=phone, birth_date = bdate, gender=gender)
            employe.save()
            return render(request,'details.html', {'name':name})
    