 
from rest_framework import viewsets
from .models import Course
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
class ReviewViewSets(ModelViewSet):
    queryset = Review.objects.all()
    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='courses',
        many=True,
        write_only=True
    )
    students_ids = serializers.PrimaryKeyRelatedField(
        queryset = Student.objects.all() ,
        source = 'student' ,
        many = True ,
        write_only = True ,
    )
    # filter_backends = [DjangoFilterBackend] 
    serializer_class = ReviewSerializer
    class Meta:
        models = Review
        fields =['id']