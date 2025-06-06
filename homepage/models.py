from django.db import models
from media.models import *
# Create your models here.
 
class Banners(models.Model):
    title = models.CharField(max_length=100 , blank=True , null=True)
    image = models.ManyToManyField(Media, related_name='image') 
    def __str__(self):
        return self.title
class SEO(models.Model):
    title = models.CharField(max_length=255, help_text="The title of the page for SEO.")
    logo = models.ManyToManyField(Media, related_name='imagess') 
    description = models.TextField(help_text="The meta description of the page.")
    keywords = models.CharField(max_length=255, help_text="Comma-separated keywords for SEO.")
    canonical_url = models.URLField(help_text="Canonical URL to avoid duplicate content issues.")
    address =  models.CharField(max_length=255,   blank=True, null=True)
    contact_number = models.CharField(max_length=255 , blank=True , null= True)
    whatsapp_number = models.CharField(max_length=255, blank=True, null=True) 
    youtube_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    scripts = models.TextField(blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    
    def get_keywords(self): 
        return self.keywords.split(',') if self.keywords else []
class FAQ(models.Model):
    course =   models.ForeignKey(Course, on_delete=models.CASCADE , null= True , blank=True, related_name='faqs' ,help_text="Leave blank for homepage" )
    question =  models.CharField(max_length=5000, blank=True, null=True) 
    answer =    models.CharField(max_length=5000, blank=True, null=True) 
    def __str__(self):
        return self.question
    
    

from django.db import models

class Facility(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()  # You can also use an ImageField if you're storing images in your project

    def __str__(self):
        return self.title
    

class home_page_data(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title