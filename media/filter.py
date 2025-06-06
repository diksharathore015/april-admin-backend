import django_filters 
from .models import *

# class CourseFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive contains
#     slug_field = django_filters.CharFilter(lookup_expr='iexact')  # Exact match for slug
#     states = django_filters.ModelMultipleChoiceFilter(queryset=State.objects.all())  # For filtering by states
#     cities = django_filters.ModelMultipleChoiceFilter(queryset=Cities.objects.all())  # For filtering by cities

#     class Meta:
#         model = Course
#         fields = ['title', 'slug_field',  ]

class MediaFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Media
        fields = ['title',]
class MediavideoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Media_video
        fields = ['title',]