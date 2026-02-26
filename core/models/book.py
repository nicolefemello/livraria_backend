from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f'({self.id}) {self.title} ({self.quantity})'