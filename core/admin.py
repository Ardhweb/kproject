from django.contrib import admin

# Register your models here.
from .models import  UploadFile,SharedFiles

@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ("file_id",)


@admin.register(SharedFiles)
class SharedFilesAdmin(admin.ModelAdmin):
    list_display = ("id",)