from django.conf import settings

def radio_stream(request):
    return {
        'stream_url': settings.RADIO_STREAM_URL
    }