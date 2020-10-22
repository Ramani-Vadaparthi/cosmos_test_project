from django.db import models


# Create your models here.


class Product(models.Model):
    product_family = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    last_updated_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    enabled_flag = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Productfamily'
        verbose_name_plural = 'Productfamily'
