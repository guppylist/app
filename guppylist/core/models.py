from django.db import models
from django.contrib.auth.models import User

ACTION_SAVE_INSERT = 'insert'
ACTION_SAVE_UPDATE = 'update'

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self):
        """
        Override model save method to modify the object before and after saving.
        """
        instance = super(BaseModel, self)

        if self.id:
            action = ACTION_SAVE_UPDATE
        else:
            action = ACTION_SAVE_INSERT

        # Before save
        try:
            self.before_save(action)
        except AttributeError:
            pass

        # The save
        instance.save()

        # After save
        try:
            self.after_save(action)
        except AttributeError:
            pass

        return instance

    def is_loaded(self):
        """
        Checks to see if the object is loaded.
        """
        if self.id is not None:
            return True
        else:
            return False

class ContentModel(BaseModel):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255)
    user = models.ForeignKey(User, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        abstract = True