from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
# 跳转用户管理页
from django.views.decorators.csrf import csrf_exempt

from knowledgePlatform.User import user_service
from knowledgePlatform.util.action_enum import ActionEnum
from knowledgePlatform.util.request2obj import response_body, queryset2dict, queryset2defined_dict


def go_user_list(request):
    return render(request, 'user/user_list.html')


# 获取所有的用户不分页
@csrf_exempt
def get_user_list(request):
    return response_body(True, ActionEnum.EXECUTE, queryset2defined_dict(user_service.get_user_list(), "username", "id"))
