from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from knowledgePlatform.top_type import top_type_service
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
# @csrf_exempt 关闭csrf验证
from knowledgePlatform.top_type.models import TopType


# 创建顶级分类
@csrf_exempt
def create_top_type(request):
    flag = top_type_service.creat_type(request.POST['top_type_name'])
    if flag == 'ok':
        context = dict()
        context['msg'] = '添加成功'
        context['code'] = '1'
        response = JsonResponse(context)
        return response


# 修改分类信息
@csrf_exempt
def update_top_type(request):
    top_type_id = request.POST['top_type_id']
    top_type_name = request.POST['top_type_name']
    is_active = request.POST['is_active']
    _top_type = TopType()
    _top_type.is_active = is_active
    _top_type.type_name = top_type_name
    _top_type.id = top_type_id
    flag = top_type_service.update_top_type(_top_type)
    if flag == 'ok':
        context = dict()
        context['msg'] = '修改成功'
        context['code'] = '1'
        response = JsonResponse(context)
        return response


# 查询分类信息
@csrf_exempt
def findall_top_type(request):
    _top_type_all = top_type_service.findall_top_type();
    context = dict()
    context['msg'] = '查询成功'
    context['code'] = '1'
    context['data'] = _top_type_all
    response = JsonResponse(context)
    return response
