from django.db import models
from .client import Client
from .products import Product


class Bill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    nit = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    product = models.ManyToManyField(Product)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, editable=False
    )
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.company_name)
