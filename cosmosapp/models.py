from djongo import models

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


class Prod(models.Model):
    product_familys = models.CharField(max_length=100, blank=True, null=True)
    creation_dates = models.DateField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    last_updated_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    enabled_flag = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Productfamily'
        verbose_name_plural = 'Productfamily'

class Indust(models.Model):
    Industry = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    last_updated_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    enabled_flag = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Indust'
        verbose_name_plural = 'Industrs'

class mount(models.Model):
    mounts = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    last_updated_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    enabled_flag = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'mount'
        verbose_name_plural = 'mounttype'


class Post(models.Model):
    title = models.CharField(max_length=50)
    texts = models.TextField(max_length=60)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Blog(models.Model):
    blogs = models.CharField(max_length=50)
    texts = models.TextField(max_length=60)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'