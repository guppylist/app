from django.conf import settings
from guppylist.contrib.list.models import List

def view_variables(request):
    page_title = ''
    if hasattr(request, 'page_title'):
        page_title = request.page_title

    q = ''
    if request.GET.get('q'):
        q = request.GET.get('q')

    return {
        'google_analytics_id': settings.GOOGLE_ANALYTICS_ID,
        'facebook_app_id': settings.FACEBOOK_APP_ID,
        'page_title': page_title,
        'q': q,
        'scripts': request.scripts,
        'user_lists': List.objects.filter(user=request.user),
    }

def status_messages(request):
    return {}
    return {
        'status_messages': {
            'success': ['This is a success message', 'This is an error message'],
            'error': ['This is an error message', 'This is an error message'],
        },
    }