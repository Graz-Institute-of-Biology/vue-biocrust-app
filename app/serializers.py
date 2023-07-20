from rest_framework import serializers
from .models import Posts, Tests, Image, ImageNew, PredResults, Document, DSetDocument, Dataset, DLModel


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
        model = DSetDocument
        fields = '__all__' 

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DLModel
        fields = '__all__' 

class PredSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredResults
        fields = '__all__'

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'