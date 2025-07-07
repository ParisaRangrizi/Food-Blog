# posts/serializers.py
from rest_framework import serializers
from . import models


class SocialPostSerializedr(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SocialPost
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
