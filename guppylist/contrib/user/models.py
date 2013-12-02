from django.db import models
from django.contrib.auth.models import User
from guppylist.core.models import BaseModel
from guppylist.contrib.list.models import List

class Profile(BaseModel):
    user = models.OneToOneField(User)

    def get_lists(self):
        """
        Get a list of the user's lists.
        """
        return List.objects.filter(user=self.user)