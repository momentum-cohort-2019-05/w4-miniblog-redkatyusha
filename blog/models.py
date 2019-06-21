from django.db import models
from django.urls import reverse
from datetime import date

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a short summary of the blog post.")
    pubdate = models.DateField(date.today())
    body_text = models.TextField

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post', args=[str(self.id)])

    class Meta:
        ordering = ['-pubdate', 'blogger']

class Blogger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'