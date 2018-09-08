from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=30, null=False)
    belonging = models.IntegerField(default=1) # Large Category Index

    def __str__(self):
        return self.categoryName

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(default=timezone.now)
    categoryList = tuple([(cat.categoryName, cat.categoryName) for cat in Category.objects.all()])

    category = models.CharField(
        max_length=20,
        choices=categoryList,
        default=categoryList[0],
    )
    

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title

