"""
Helper model class for GuppyList API.

Defines models for persisting and querying score data on a per user basis and
provides a method for returning a 401 Unauthorized when no current user can be
determined.
"""
import logging

from google.appengine.ext import ndb

from messages.item import Item as ItemMessage


class ItemModel(ndb.Model):
    """Model to store list item that have been inserted by users."""
    title = ndb.StringProperty(required=True)
    notes = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def _get_kind(cls):
        return 'Item'

    def to_message(self, current=False):
        """Turns the Item entity into a ProtoRPC object.

        Returns:
            An instance of Item with the ID set to the datastore
            ID of the current entity, the outcome simply the entity's outcome value.
        """
        item = ItemMessage()
        item.id = self.key.id()
        item.title = self.title
        item.notes = self.notes
        item.created = self.created
        item.updated = self.updated

        return item