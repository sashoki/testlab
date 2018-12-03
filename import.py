import csv, sys, os

project_dir = '/var/www/testlab/bin/testlab/testlab/'

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from createcsv.models import Customer

data = csv.reader(open('/var/www/testlab/bin/testlab/TestData.csv'), delimiter=",")

for row in data:
    if row[0] != 'FirstName':
        customer = Customer()
        customer.FirstName = row[0]
        customer.LastName = row[1]
        customer.BirthDate = row[2]
        customer.RegistrationDate = row[3]
        customer.save()