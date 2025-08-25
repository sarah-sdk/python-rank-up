from rest_framework import viewsets
from .models import BucketItem
from .serializers import BucketItemSerializer

class BucketViewSet(viewsets.ModelViewSet):
  queryset = BucketItem.objects.all()
  serializer_class = BucketItemSerializer

  def get_queryset(self):
    return BucketItem.objects.filter(user=self.request.user)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)