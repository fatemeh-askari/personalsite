from datetime import timezone

from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    answer_admin = models.TextField(null=True, blank=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Contact us"
        verbose_name_plural = "Contact us"

    def __str__(self):
        return f'{self.name} by {self.email} on {self.subject}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/')
    categories = models.ManyToManyField(Category)
    link = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=300,verbose_name='slug', blank=True, null=True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, null=True, verbose_name='image')
    body = models.TextField(verbose_name='text', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')

    def __str__(self):
        return self.title
