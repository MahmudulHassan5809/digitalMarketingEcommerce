from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import Tag
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to="category/%Y/%m/%d/")
    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        full_path = [self.category_name]
        k = self.parent
        while k is not None:
            full_path.append(k.category_name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Store(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_store')
    store_name = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    banner = models.ImageField(upload_to="store/")

    def __str__(self):
        return self.store_name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_products")

    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name="store_products")

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    description = RichTextUploadingField()
    price = models.FloatField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name
