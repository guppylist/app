"""ProtoRPC message class definitions for Musubio API."""

from protorpc import messages, message_types

class List(messages.Message):
    """List that stores a message."""
    id = messages.IntegerField(1, required=True)
    title = messages.StringField(3, required=True)
    description = messages.StringField(4, required=False)
    created = message_types.DateTimeField(6, required=False)
    updated = message_types.DateTimeField(7, required=False)


class ListDetailsRequest(messages.Message):
    """ProtoRPC message definition to represent a channel to be fetched."""
    id = messages.IntegerField(1, required=True)


class ListInsertRequest(messages.Message):
    """ProtoRPC message definition to represent a list to be inserted."""
    title = messages.StringField(1, required=True)
    description = messages.StringField(2, required=False)


class ListDeleteRequest(messages.Message):
    """ProtoRPC message definition to represent a list to be deleted."""
    id = messages.IntegerField(1, required=True)


class ListListResponse(messages.Message):
    """Collection of Lists."""
    lists = messages.MessageField(List, 1, repeated=True)
