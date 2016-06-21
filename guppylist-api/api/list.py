"""
GuppyList API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""
import endpoints, logging
from protorpc import message_types
from protorpc import remote
from api import api_root

from google.appengine.api import memcache

from messages.list import List, ListDetailsRequest, ListListResponse, ListInsertRequest, ListDeleteRequest
from models.list import ListModel

package = 'Guppylist'

@api_root.api_class(resource_name='guppylist')
class ListApi(remote.Service):
    """GuppyList List API v1"""
    @endpoints.method(message_types.VoidMessage,
                      ListListResponse,
                      path='lists',
                      http_method='GET',
                      name='lists.list')
    def list_list(self, request):
        logging.info('list_list()')

        query = ListModel.get_lists()
        lists = [entity.to_message() for entity in query.fetch()]

        listList = ListListResponse()
        listList.lists = lists

        return listList


    @endpoints.method(ListDetailsRequest,
                      List,
                      path='lists/{id}',
                      http_method='GET',
                      name='channels.details')
    def list_details(self, request):
        logging.info('list_details()')

        list = ListModel.get_details(request)

        return list.to_message()


    @endpoints.method(ListInsertRequest,
                      List,
                      path='lists',
                      http_method='POST',
                      name='lists.insert')
    def list_insert(self, request):
        logging.info('list_insert()')

        entity = ListModel.put_from_message(request)
        return entity.to_message()


    @endpoints.method(ListDeleteRequest,
                      ListListResponse,
                      path='lists/{id}',
                      http_method='DELETE',
                      name='list.delete')
    def list_delete_all(self, request):
        logging.info('list_delete()')

        ListModel.delete_by_id(request)

        return ListListResponse()
