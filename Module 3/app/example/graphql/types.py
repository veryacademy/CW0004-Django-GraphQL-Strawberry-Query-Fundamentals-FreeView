# types.py

import strawberry


@strawberry.type
class CategoryType:
    id: strawberry.ID
    parent_id: int | None
    name: str
    slug: str
    is_active: bool
    level: int