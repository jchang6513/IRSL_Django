from rest_framework import serializers
from .models import ClassName, Course

class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    classdate = serializers.CharField(source='class_name.date')
    classname = serializers.CharField(source='class_name.name')
    class Meta:
        model = Course
        fields = ('class_name','classdate','classname', 'date', 'title', 'handout', 'handout_type')
