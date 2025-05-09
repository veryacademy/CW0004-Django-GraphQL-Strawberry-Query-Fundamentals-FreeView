from django.contrib import admin
from .models import (
    Category, PromotionEvent, Product, ProductPromotionEvent,
    StockManagement, User, Order, OrderProduct
)

# Register all models to the admin site
admin.site.register(Category)
admin.site.register(PromotionEvent)
admin.site.register(Product)
admin.site.register(ProductPromotionEvent)
admin.site.register(StockManagement)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderProduct)