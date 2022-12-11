import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from pizzas.models import *

'''
pizzas = Pizza.objects.all()

print(pizzas)

for p in pizzas:
    print(p)
    print(p.pizza_name)
'''

p = Pizza.objects.get(id=1)
print(p)

toppings = Topping.objects.filter(pizza=p)

for t in toppings:
    print(t)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username)
    print(user.last_login)