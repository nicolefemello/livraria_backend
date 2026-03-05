from django.db import models

from .category import Category
from .publisher import Publisher
from .author import Author


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books', null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books', blank=True)

    def __str__(self):
        return f'({self.id}) {self.title} ({self.quantity})'
