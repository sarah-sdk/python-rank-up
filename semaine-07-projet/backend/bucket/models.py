from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
  ('travel', 'voyage'),
  ('reading', 'lecture'),
  ('exp', 'expérience'),
  ('sport', 'sport'),
  ('skill', 'compétence'),
  ('other', 'autre')
]

class BucketItem(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  done = models.BooleanField(default=False)
  category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{'✅' if self.done else '❌'} {self.name}"