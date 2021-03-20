from django.db import models

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='service')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='service'
        verbose_name_plural='services'

    def __srt__(self):
        return self.title