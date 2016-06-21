"""ProtoRPC message class definitions for GuppyList API."""

from protorpc import messages, message_types

class Item(messages.Message):
    """List that stores a message."""
    id = messages.IntegerField(1, required=True)
    title = messages.StringField(3, required=True)
    note = messages.StringField(4, required=False)
    created = message_types.DateTimeField(6, required=False)
    updated = message_types.DateTimeField(7, required=False)

