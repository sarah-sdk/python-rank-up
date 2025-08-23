from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  filterset_fields = ['done']
  ordering_fields = ['created_at', 'title']
  ordering = ['created_at']

  def get_queryset(self):
    return Task.objects.filter(user=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)