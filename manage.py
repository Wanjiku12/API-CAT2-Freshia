from django.db import models

class Customer(models.Model):
    first_name  = models.CharField(max_length=100, help_text="Full name of the customer.")
    email = models.EmailField(unique=True, help_text="Unique email address of the customer.")
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, help_text="Phone number of the customer.")
    address = models.CharField(max_length=200, help_text="Address of the customer.")
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email}) (Phone: {self.phone_number}) (Address: {self.address})"

class Order(models.Model):
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name='orders',
        help_text="The customer who placed the order."
    )
    order_date = models.DateTimeField(auto_now_add=True, help_text="Date and time when the order was placed.")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount for the order.")

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"
class Meta:
    ordering = ["-order_date"]  # Orders listed with newest first
