from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    # owner = 
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True,)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=1000,null=True, blank=True)
    source_link = models.CharField(max_length=1000,null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''

        return img


class Review(models.Model):

    vote_type = (
        ('up','up'),
        ('down','down')
    )
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True,related_name='reviews')
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=100,choices=vote_type)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

