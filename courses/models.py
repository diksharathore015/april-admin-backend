from django.db import models
from location.models import *
from django.utils.text import slugify
class Course(models.Model):
    title = models.CharField(max_length=5550)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slider_images = models.JSONField(default=list, blank=True)
    meta_title = models.CharField(max_length=1000, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=1000, blank=True, null=True)
    contact_number = models.CharField(max_length=1000, blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    state = models.ManyToManyField(State, related_name='state') 
    city = models.ManyToManyField(City, related_name='city') 
    locality = models.ManyToManyField(Locality, related_name='locality') 
    student_list =  models.JSONField(default=list, blank=True, null=True) 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    
