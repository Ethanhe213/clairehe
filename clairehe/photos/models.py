from django.db import models
from .validators import validate_file_extension
from PIL import Image
from PIL.ExifTags import TAGS
class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name
class Photo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(upload_to='images',null=False,blank=False)
    created_at=models.DateTimeField(null=True, blank=True)
    description=models.TextField()
    def __str__(self):
        return self.image.url
class Category_video(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name
class Video(models.Model):
    category=models.ForeignKey(Category_video,on_delete=models.SET_NULL,null=True,blank=True)
    video = models.FileField(upload_to='videos',null=True,
    validators=[validate_file_extension])
    description=models.TextField()
    created_at=models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.description
# Create your models here.
