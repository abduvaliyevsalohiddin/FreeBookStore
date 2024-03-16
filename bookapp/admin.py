from django.contrib import admin
from bookapp.models import *
from uploadapp.models import Upload

admin.site.register([Author, BookCategory])


class ImageInline(admin.TabularInline):
    model = BookImage
    fields = ('image',)


class UploadInline(admin.TabularInline):
    model = Upload
    fields = ('file',)


class BookAdmin(admin.ModelAdmin):
    inlines = [ImageInline, UploadInline]


admin.site.register(Book, BookAdmin)
