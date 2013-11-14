from django.conf import settings

def view_variables(request):
    page_title = ''
    if hasattr(request, 'page_title'):
        page_title = request.page_title

    return {
      'google_analytics_id': settings.GOOGLE_ANALYTICS_ID,
      'page_title': page_title,
      'q': request.GET.get('q'),
    }

def status_messages(request):
    return {}
    return {
        'status_messages': {
            'success': ['This is a success message', 'This is an error message'],
            'error': ['This is an error message', 'This is an error message'],
        },
    }