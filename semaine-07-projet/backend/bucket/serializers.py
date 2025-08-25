from rest_framework import serializers
from .models import BucketItem

class BucketItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = BucketItem
    fields = ['id', 'user', 'name', 'done', 'category']
    read_only_fields = ['id', 'user']