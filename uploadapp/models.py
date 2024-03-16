from django.db import models
from bookapp.models import Book
from userapp.models import UserAdmin


class Rate(models.Model):
    grade = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(UserAdmin, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.book}'


class Download(models.Model):
    user = models.ForeignKey(UserAdmin, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.book}'


class Upload(models.Model):
    file = models.FileField(upload_to='books')
    date = models.DateField(auto_now_add=True)

    book = models.OneToOneField(Book, on_delete=models.CASCADE)


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAdmin, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.book}'
