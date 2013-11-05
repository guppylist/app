from django.conf import settings

def view_variables(request):
    return {
      'google_analytics_id': settings.GOOGLE_ANALYTICS_ID,
    }

def status_messages(request):
    return {}
    return {
        'status_messages': {
            'success': ['This is a success message', 'This is an error message'],
            'error': ['This is an error message', 'This is an error message'],
        },
    }