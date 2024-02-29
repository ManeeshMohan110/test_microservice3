from django.db import models

from django.db import models

class Order(models.Model):
    user_id = models.PositiveIntegerField()  # Store user_id instead of foreign key
    product_id = models.PositiveIntegerField()  # Store product_id instead of foreign key
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


