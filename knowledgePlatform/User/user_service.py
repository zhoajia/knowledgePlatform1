from django.contrib.auth.models import User


def get_user_list():
    user_list = User.objects.filter(is_active=1)
    return user_list
