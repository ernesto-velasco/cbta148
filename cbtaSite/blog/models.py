from django.db import models
from django.utils import timezone

# Post de las noticias que se publican en la pagina principal
class Post(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        banner_image = models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d/files')
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title

class PostImage(models.Model):
    property = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/images')
class PostFile(models.Model):
    property = models.ForeignKey(Post, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='posts/%Y/%m/%d/files')