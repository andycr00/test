from .models import Client, Product, Bill
from django.contrib.auth.models import User
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prueba_quick.settings")

import django

django.setup()


def run_seed():
    User.objects.create_superuser('test', 'test@test.com', '123456')

    client_data = [
        {"document": "123", "first_name": "Andres", "last_name": "Felipe"},
        {"document": "456", "first_name": "Juan", "last_name": "Gabriel"},
        {"document": "789", "first_name": "Daniel", "last_name": "Esteban"},
        {"document": "159", "first_name": "Laura", "last_name": "Marcela"},
    ]

    for datos in client_data:
        Client.objects.create(**datos)

    product_data = [
        {"name": "Test 1", "description": "Test 1"},
        {"name": "Test 2", "description": "Test 2"},
        {"name": "Test 3", "description": "Test 3"},
        {"name": "Test 4", "description": "Test 4"},
        {"name": "Test 5", "description": "Test 5"},
    ]

    bill_data = [
        {"company_name": "Andres Felipe", "nit": "123", "code": "123", "client_id": 1},
        {"company_name": "Juan Gabriel", "nit": "456", "code": "456", "client_id": 2},
        {"company_name": "Daniel Esteban", "nit": "789", "code": "789", "client_id": 3},
        {"company_name": "Laura Marcela", "nit": "159", "code": "159", "client_id": 4},
    ]

    for i in range(len(bill_data)):
        product = Product.objects.create(**product_data[i])
        bill = Bill.objects.create(**bill_data[i])
        bill.product.add(product)


if __name__ == "__main__":
    run_seed()
