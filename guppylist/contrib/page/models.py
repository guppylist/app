from django.db import models
from guppylist.core.models import BaseModel

class Signup(BaseModel):
    email = models.EmailField(null=False)
    create_date = models.DateTimeField(auto_now_add=True)