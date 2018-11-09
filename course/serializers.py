from rest_framework import serializers
from .models import ClassName, Course

class CourseSerializer(serializers.ModelSerializer):
#    classdate = serializers.CharField(source='class_name.date')
#    classname = serializers.CharField(source='class_name.name')
    class Meta:
        model = Course
        order_by = (('-date',))
#        fields = ('class_name','classdate','classname', 'date', 'title', 'handout', 'handout_type')
        fields = ('date', 'title', 'handout', 'handout_type')

class ClassNameSerializer(serializers.ModelSerializer):
    lectures = serializers.SerializerMethodField()
    appendices = serializers.SerializerMethodField()
    class Meta:
        model = ClassName
        fields = ('date', 'name', 'lectures', 'appendices')
    def get_lectures(self, instance):
        lectures = instance.course_set.all().filter(handout_type='LC').order_by('date')
        return CourseSerializer(lectures, many=True).data
    def get_appendices(self, instance):
        appendices = instance.course_set.all().filter(handout_type='AP').order_by('date')
        return CourseSerializer(appendices, many=True).data
