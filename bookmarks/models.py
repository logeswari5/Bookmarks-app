
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class bookmarks(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Add description of bookmark')
    tag = TaggableManager()

    def get_absolute_url(self):
        return reverse('bookmarks-detail', args=[str(self.id)])

    def __str__(self):
        return self.name