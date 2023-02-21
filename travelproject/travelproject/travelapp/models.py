from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class own(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    note=models.TextField()

    def __str__(self):
        return  self.name