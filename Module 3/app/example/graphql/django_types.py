# types.py

import strawberry_django
from inventory.models import Category

@strawberry_django.type(Category, fields=("id", "name",), description="A product category in the inventory system")
class CategoryType:
    pass