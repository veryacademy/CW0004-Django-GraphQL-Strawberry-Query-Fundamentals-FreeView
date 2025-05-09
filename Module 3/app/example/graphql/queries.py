# queries.py

import strawberry
from .django_types import CategoryType
from typing import List
from inventory.models import Category


@strawberry.type
class Query:
    @strawberry.field(description="Returns a list of all categories")
    def categories(self) -> List[CategoryType]:
       return Category.objects.only("id", "name")


# @strawberry.type
# class Query:
#     @strawberry.field
#     def categories(self) -> List[CategoryType]:
#        return [
#             CategoryType(
#                 id="1",
#                 parent_id=None,
#                 name="Books",
#                 slug="books",
#                 is_active=True,
#                 level=0
#             ),
#             CategoryType(
#                 id="2",
#                 parent_id=1,
#                 name="Fiction",
#                 slug="fiction",
#                 is_active=True,
#                 level=1
#             ),
#         ]



