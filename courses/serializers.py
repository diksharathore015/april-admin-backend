from rest_framework import serializers
from location.models import State, City, Locality
from .models import Course
from location.serializers import *
class CourseSerializer(serializers.ModelSerializer):
    # Use nested serializers for related models
    state = StatesNestedSerializer(many=True, read_only=True)
    city = CityNestedSerializer(many=True, read_only=True)
    locality = LocalitiesNestedSerializer(many=True, read_only=True)
    student_list = serializers.JSONField()
    state_ids = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(),
        source='state',
        many=True,
        write_only=True
    )
    city_ids = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city',
        many=True,
        write_only=True
    )
    localities_ids = serializers.PrimaryKeyRelatedField(
        queryset=Locality.objects.all() ,
        source='locality',
        many=True,
        write_only=True
    )
    class Meta:
        model = Course
        fields = [
            'id', 'title', 'short_description', 'description', 'slider_images', 
            'meta_title', 'meta_description', 'meta_keywords', 'contact_number', 
            'youtube_link', 'facebook_link', 'instagram_link', 'created_at', 
            'updated_at', 'slug', 'state', 'city', 'locality' ,'state_ids' , 'city_ids' ,'localities_ids' ,'student_list'
        ]
    def validate_title(self, value):
        
        if Course.objects.filter(title=value).exists():
            raise serializers.ValidationError("A course with this title already exists.")
        return value
class CourseTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title'] 
