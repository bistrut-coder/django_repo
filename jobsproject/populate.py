import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')
django.setup()

from testapp.models import Hybdjobs,Bngjobs,Punejobs
from faker import Faker
fake=Faker()
from random import *


def gen_phone_no():
    p=randint(6,9)
    num=''+str(p)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fcompany=fake.company
        ftitle = fake.random_element(elements=('Project Manager', 'Team Lead', 'Software Engineer', 'HR', 'Associate Engineer'))
        fphonenumber=gen_phone_no()
        femail=fake.email()
        fdate=fake.date()
        hydb_jobs_record=Hybdjobs.objects.get_or_create(
            company=fcompany,
            title=ftitle,
            phonenumber=fphonenumber,
            email=femail,
            dob=fdate,
        )
n=int(input('Enter number of company:'))
populate(n)
print(f'{n} number of company inserted successfully.... ')

