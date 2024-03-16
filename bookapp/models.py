from userapp.models import UserAdmin
from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.full_name


class BookCategory(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    num_downloaded = models.IntegerField(default=0)
    user = models.ForeignKey(UserAdmin, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BookImage(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')

