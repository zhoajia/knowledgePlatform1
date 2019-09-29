from django.shortcuts import render

# Create your views here.
# 跳转角色列表页
from django.views.decorators.csrf import csrf_exempt

from knowledgePlatform.krole import role_service
from knowledgePlatform.krole.models import KroleEntity
from knowledgePlatform.util.action_enum import ActionEnum
from knowledgePlatform.util.request2obj import queryset2dict, response_body, request2obj, queryset2defined_dict


@csrf_exempt
def go_role_list(request):
    return render(request, 'permission/role_list.html')


@csrf_exempt
def get_role_list(request):
    role_list, total = role_service.get_role_list(request.POST["page_number"])
    return response_body(True, ActionEnum.EXECUTE, queryset2dict(KroleEntity(), role_list), total)


@csrf_exempt
def create_role(request):
    role_entity = request2obj(KroleEntity(), request)
    flag = role_service.create_role(role_entity)
    if flag:
        return response_body(flag, ActionEnum.ADD, None)
    else:
        return response_body(flag, ActionEnum.SAME_ADD, None)


@csrf_exempt
def get_user_by_role_id(request):
    user_list = role_service.get_user_by_role_id(request.POST['role_id'])
    return response_body(True, ActionEnum.EXECUTE, queryset2defined_dict(user_list,'id','username'))


# 根据给定的角色id查询所配置的权限
@csrf_exempt
def get_permissions_by_role_id(request):
    permission_list = role_service.get_permissions_by_role_id(request.POST['role_id'])
    return response_body(True, ActionEnum.EXECUTE, queryset2defined_dict(permission_list, 'id'))