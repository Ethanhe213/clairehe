from django.db import models
from .validators import validate_file_extension
class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name
class Photo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(null=False,blank=False)
    description=models.TextField()
    def __str__(self):
        return self.description
class Category_video(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name
class Video(models.Model):
    category=models.ForeignKey(Category_video,on_delete=models.SET_NULL,null=True,blank=True)
    video = models.FileField(upload_to='static/videos',null=True,
    validators=[validate_file_extension])
    description=models.TextField()
    def __str__(self):
        return self.description
# Create your models here.
