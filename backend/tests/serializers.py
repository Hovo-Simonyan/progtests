from rest_framework import serializers
from .models import Test, Question
from django.contrib.auth.models import User


class LanguageSerializer(serializers.ModelSerializer):
    """ Serializer for languages. """

    class Meta:
        model = Test
        fields = ('name', 'about', 'short_description','image', 'level', 'category')

class QuestionSerializer(serializers.ModelSerializer):
    """ Serializer for question. """

    class Meta:
        model = Question
        fields = ('question', 'image', 'answers')
        depth = 1