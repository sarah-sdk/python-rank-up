from rest_framework import viewsets
from .models import BucketItem
from .serializers import BucketItemSerializer

class BucketViewSet(viewsets.ModelViewSet):
  queryset = BucketItem.objects.all()
  serializer_class = BucketItemSerializer