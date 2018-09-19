from .models import JYLiu_CV, Member, Past, Graduate
from rest_framework import serializers

class JYLSerializer(serializers.ModelSerializer):
    class Meta:
        model = JYLiu_CV
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class PastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Past
        fields = '__all__'

class GraduateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduate
        fields = '__all__'
