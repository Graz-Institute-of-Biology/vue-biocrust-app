from rest_framework import serializers
from .models import Posts, Tests, Image, ImageNew


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__' 

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = '__all__' 

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__' 

class ImageNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNew
        fields = '__all__' 