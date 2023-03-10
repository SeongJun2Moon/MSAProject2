from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Posts.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass