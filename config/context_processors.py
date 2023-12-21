from django.conf import settings

def my_setting(request):
    return {'MY_SETTING': settings}


# Add the 'ENVIRONMENT' setting to the template context
def environment(request):
    return {'ENVIRONMENT': settings.ENVIRONMENT}
