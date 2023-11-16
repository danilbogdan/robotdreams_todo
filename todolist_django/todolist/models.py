# todo/models.py
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Task(MPTTModel):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def get_descendants(self, *args):
        return super().get_descendants(include_self=False)
    
    def __repr__(self):
        return str(self.title)
    
    def __str__(self):
        return str(self.title)
