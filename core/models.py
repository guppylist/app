import datetime

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class BaseModel(models.Model):
    class Meta:
        abstract = True


class ContentModel(BaseModel):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    user = models.ForeignKey(User)
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Publish')