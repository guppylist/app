"""
Helper model class for GuppyList API.

Defines models for persisting and querying score data on a per user basis and
provides a method for returning a 401 Unauthorized when no current user can be
determined.
"""
import logging

from google.appengine.ext import ndb

from messages.list import List as ListMessage


class ListModel(ndb.Model):
    """Model to store lists that have been inserted by users."""
    title = ndb.StringProperty(required=True)
    description = ndb.StringProperty()
    # items = ndb.StructuredProperty(ItemModel, repeated=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def _get_kind(cls):
        return 'List'

    def to_message(self, current=False):
        """
        Turns the List entity into a ProtoRPC object.

        Returns:
            An instance of List with the ID set to the datastore
            ID of the current entity, the outcome simply the entity's outcome value.
        """
        list = ListMessage()
        list.id = self.key.id()
        list.title = self.title
        list.description = self.description
        list.created = self.created
        list.updated = self.updated

        return list

    @classmethod
    def get_details(cls, message):
        return cls.get_by_id(message.id)

    @classmethod
    def get_lists(cls):
        return cls.query()

    @classmethod
    def put_from_message(cls, message):
        """Gets the current user and inserts a list.

        :param message:
        :return:
        """
        # current_user = get_endpoints_current_user()
        # entity = cls(outcome=message.outcome, player=current_user)
        entity = cls(title=message.title, description=message.description)
        entity.put()
        return entity

    @classmethod
    def delete_by_id(cls, message):
        """Delete a list by ID

        :param message:
        :return:
        """
        logging.info('delete_by_id()')

        entity = cls.get_by_id(message.id)
        ndb.delete_multi(keys=[entity.key])