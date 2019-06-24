from django.db import models
from django.urls import reverse
from datetime import date

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a short summary of the blog post.")
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    body_text = models.TextField(max_length=1000000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post', args=[str(self.id)])

    class Meta:
        ordering = ['-date_posted', 'blogger']

class Blogger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'