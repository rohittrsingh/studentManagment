from rest_framework import serializers
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SchoolStudentSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True, source="school_student")

    class Meta:
        model = School
        fields = '__all__'
