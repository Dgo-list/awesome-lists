from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Name", max_length=100)

    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField("Name", max_length=250)

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

class Item(models.Model):
    sub_cat = models.ForeignKey(SubCategory)
    url = models.URLField("URL")
    title = models.CharField("Title", max_length=250)
    description = models.TextField("Description")
    created_at = models.DateTimeField("Created At")
