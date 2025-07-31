from django.db import models

# Create your models here.
class Review(models.Model):
    book = models.ForeignKey('Book', blank=True, null=True, on_delete=models.CASCADE, related_name='reviews')
    user = models.ManyToManyField('User', related_name='reviews', blank=True)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.book.title} - {self.rating}"

class Book(models.Model):
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    title = models.CharField('Title', max_length=200)
    author = models.CharField('Author', max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username