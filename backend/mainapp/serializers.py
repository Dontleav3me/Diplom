from rest_framework import serializers
from .models import project, Directions, News, BottomNews, MiniNew, SoloNews,NewsTop

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

class DirectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directions
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class BottomNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomNews
        fields = '__all__'

class MiniNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniNew
        fields = '__all__'

class SoloNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoloNews
        fields = '__all__'

class NewsTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTop
        fields = '__all__'