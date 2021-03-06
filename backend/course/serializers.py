from rest_framework import serializers
from course.models import Course, Lesson, Comment


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description')

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description', 'long_description')

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'slug', 'short_description', 'long_description')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = ('id', 'name', 'content', 'created_at')