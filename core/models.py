from django.db import models

# Create your models here.
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class UploadFile(models.Model):
    file_id = models.CharField(max_length=255, default=uuid.uuid4().hex[:12], editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) 
    uploading_file = models.FileField(upload_to='uploads/file/documents/%Y/%m/%d') 
    description = models.TextField(blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return f"{self.file_id}"

    def get_thumbnail(self):
        if self.uploading_file.url.endswith('.jpg') or self.uploading_file.url.endswith('.jpeg')or  self.uploading_file.url.endswith('.png') or  self.uploading_file.url.endswith('.webmp'):
            #print(True)
            # print(f"URL:{self.uploading_file.url}")
            return self.uploading_file.url

  
          
class SharedFiles(models.Model):
    sharefiles = models.ForeignKey(UploadFile,on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)
    access_level = models.CharField(max_length=255, choices=[('read-only', 'Read Only'), ('read-write', 'Read and Write')], default='read-only')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
    