from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from knowledgePlatform.kpermissions import permission_service
from knowledgePlatform.kpermissions.models import KpermissionsEntity
from django.core import serializers
import json

from knowledgePlatform.util.action_enum import ActionEnum
from knowledgePlatform.util.queryUtil import ResultDate
from knowledgePlatform.util.request2obj import response_body, request2obj, queryset2dict


# 跳转权限列表页
@csrf_exempt
def go_permission_list(request):
    return render(request, 'permission/permission_list.html')


# 分页获取所有的权限
@csrf_exempt
def get_permission_list(request):
    permission_entity = KpermissionsEntity()
    permission_list, total = permission_service.get_all_permission(request.POST["page_number"])
    permission_li = queryset2dict(permission_entity, permission_list)
    return response_body(True, ActionEnum.EXECUTE, permission_li, total)


# 权限创建
@csrf_exempt
def permission_create(request):
    permission_entity = KpermissionsEntity()
    permission_entity = request2obj(permission_entity, request)
    flag = permission_service.permission_create(permission_entity)
    return response_body(flag, ActionEnum.ADD, None)


# 查询权限列表（树形加载）
@csrf_exempt
def load_permission_tree(request):
    return response_body(True, ActionEnum.EXECUTE,permission_service.load_permission_tree())