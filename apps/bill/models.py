from django.db import models
from apps.product.models import Product

# Create your models here.

class Bill(models.Model):
    customer_email = models.EmailField()
    payment_method = models.CharField(
        max_length=10,
        choices=[('cash', 'Cash'), ('card', 'Card'), ('upi', 'UPI')],
        default='cash'
    )
    # customer_paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # denomination_amounts = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bill {self.id} - {self.customer_email}"
    
    @property
    def total_without_tax(self):
        return sum(item.product_bill_amount for item in self.items.all())

    @property
    def total_tax(self):
        return sum(item.tax_amount for item in self.items.all())

    @property
    def net_price(self):
        return self.total_without_tax + self.total_tax

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    product_bill_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    @property
    def tax_amount(self):
        return (self.product_bill_amount * self.product.tax_percentage) / 100

    @property
    def total_amount(self):
        return self.product_bill_amount + self.tax_amount
