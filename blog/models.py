from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)# we havent used ()after now bcz we dont want to execute the function at this point but only pass the function to default
    author = models.ForeignKey(User, on_delete=models.CASCADE)#if the author is deleted, the post will also be deleted
    objects = models.Manager() # bcz in views.py it was showing an error that Class 'Post' has no 'objects' member as Django adds that property dynamically to all model classes (it uses a lot of magic under the hood), so the IDE doesn't know about it by looking at the class declaration, so it warns you about a possible error (it's not). so now VSC will see the objects declared and will not complain about it again.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
        




