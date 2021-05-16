from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='category')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    emails = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']



class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)



class Contact(models.Model):
    Name = models.CharField(max_length =10)
    Address= models.CharField(max_length =10)
    Email=models.CharField(max_length =10)
    phone =models.CharField(max_length =30)

    def __str__(self):
        return self.Name




class Services(models.Model):
    type = models.CharField(max_length =10)
    des = models.CharField(max_length =100)


    def __str__(self):
        return self.type
