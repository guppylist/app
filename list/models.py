from django.db import models

from core.models import ContentModel


class List(ContentModel):
    description = models.TextField()


class ListItem(ContentModel):
    notes = models.TextField()
