import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()
from AppTwo.models import User
from faker import Faker

faking = Faker()
def populate(N=10):
    for entry in range(N):
        fake_email=faking.email()
        fake_name=faking.name()
        fake_first_name=fake_name.split()[0]
        fake_last_name=fake_name.split()[1]
        person=User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')