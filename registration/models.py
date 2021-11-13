from django.db import models

# Create your models here.
class employeedata(models.Model):
    employee_name = models.CharField(max_length=25)
    #emp_id = models.CharField(max_length=25, unique=True, default=0)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    birth_date = models.DateField()
    '''
    Male = 'Male'
    Female = 'Female'
    choice = (
        (Male,'Male'),
        (Female,'Female'),
    )
    '''
    gender = models.CharField(max_length=10)