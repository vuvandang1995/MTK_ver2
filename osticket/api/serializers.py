from rest_framework import serializers
from user.models import *


class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ('id', 'name', 'status', 'description')
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Users.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.fullname = validated_data.get('fullname', instance.fullname)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance