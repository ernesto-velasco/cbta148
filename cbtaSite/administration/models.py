from django.db import models

# Create your models here.
class Basic_info(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number =  models.CharField(max_length=20)
    facebook_link = models.URLField(max_length=500)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    position = models.IntegerField()
    image = models.ImageField(upload_to='slider/%Y/%m/%d/images')
    file = models.FileField(upload_to='slider/%Y/%m/%d/files',blank=True, null=True)

class Page(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    banner_image = models.ImageField(blank=True, null=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class PageImage(models.Model):
    property = models.ForeignKey(Page, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='page/%Y/%m/%d/images')
class PageFile(models.Model):
    property = models.ForeignKey(Page, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='page/%Y/%m/%d/files')