from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class Comment(models.Model):    
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    postcomment = models.TextField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.name}'