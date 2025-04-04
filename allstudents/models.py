from django.db import models

# from courses.models import Course
from location.models import *
from media.models import *
class Student(models.Model):
    name = models.CharField(max_length=255)
    homepage = models.BooleanField(default=False)
    detail = models.CharField(max_length=500, blank=True, null=True)
    meta_title = models.CharField(max_length=500, blank=True, null=True)
    meta_descriptions = models.CharField(max_length=1000, blank=True, null=True)
    meta_keyWords = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ManyToManyField(Media,  null=True, blank=True, related_name="allstudents")
    courses = models.ManyToManyField('courses.Course', related_name='allstudents' , null=True, blank=True)
    states = models.ManyToManyField(State, related_name='allstudents' , null=True, blank=True)
    cities = models.ManyToManyField(City, related_name='allstudents' , null=True, blank=True)
    localities = models.ManyToManyField(Locality, related_name='allstudents' , null=True, blank=True)
    contact_number = models.CharField(max_length=1500, blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    rating = models.CharField(max_length=500, blank=True, null=True)
    review = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.name
