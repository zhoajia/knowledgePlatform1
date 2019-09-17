from django.shortcuts import render
from knowledgePlatform.repository import repository_service
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from knowledgePlatform.repository.models import RepositoryEntity
from knowledgePlatform.util.request2obj import request2obj


# 跳转仓库页面
def go_repository(request):
    return render(request, "repository/repository_list.html")


# 获取所有仓库
@csrf_exempt
def get_all_repository_for_webservice(request):
    l = repository_service.get_all_repository(1, 0)  # 获取webservice根仓库
    context = dict()
    context['msg'] = '查询成功'
    context['code'] = '1'
    context['data'] = l
    response = JsonResponse(context)
    return response


# 创建仓库
@csrf_exempt
def repository_create(request):
    s1 = RepositoryEntity()
    repository_entity = request2obj(s1, request)
    flag = repository_service.repository_create(repository_entity)
    context = dict()
    if flag == "ok":
        context['msg'] = '添加成功'
        context['code'] = '1'
    else:
        context['msg'] = '添加失败'
        context['code'] = '1'
    response = JsonResponse(context)
    return response