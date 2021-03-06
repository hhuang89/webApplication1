from django.db import models

# Create your models here.
from django.templatetags.static import static


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    booktype = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="booktype")
    bookname = models.CharField(max_length=128)
    authorName = models.CharField(max_length=128)
    brief = models.CharField(max_length=1024)
    bookcover1 = models.CharField(max_length=64)
    bookcover2 = models.CharField(max_length=64)
    bookcover3 = models.CharField(max_length=64)
    price = models.DecimalField(default=9.99, max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.id}: {self.bookname} and {self.authorName}"

    @property
    def img_url(self):
        return static("images/{}".format(self.bookcover1))
