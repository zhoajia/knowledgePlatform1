from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from knowledgePlatform.sub_type import sub_type_service
from knowledgePlatform.sub_type.models import SubType
from knowledgePlatform.util.action_enum import ActionEnum
from knowledgePlatform.util.request2obj import queryset2dict, response_body


# 查询所有的功能模块
@csrf_exempt
def find_all_active_sub_type(request):
    sub_type_list = sub_type_service.get_all_sub_type(request.POST["active"])
    return response_body(True, ActionEnum.EXECUTE,  queryset2dict(SubType(),sub_type_list))
