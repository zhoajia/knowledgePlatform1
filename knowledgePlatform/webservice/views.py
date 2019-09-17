from django.shortcuts import render
from knowledgePlatform.webservice import webservice_service
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# 跳转webservice页面
@csrf_exempt
def go_webservice(request):
    return render(request, "repository/webservice_list.html")


# 查询webservice
@csrf_exempt
def get_all_webservice(request):
    repository_id = request.POST['repository_id']
    all_webservice = webservice_service.get_all_webservice(repository_id)
    context = dict()
    context['msg'] = '查询成功'
    context['code'] = '1'
    context['data'] = all_webservice
    response = JsonResponse(context)
    return response


# 查询webservice信息
@csrf_exempt
def get_webservice_info(request):
    webservice_id = request.POST['webservice_id']
    webservice_info = webservice_service.get_webservice_info_by_id(webservice_id)
    context = dict()
    context['msg'] = '查询成功'
    context['code'] = '1'
    context['data'] = webservice_info
    response = JsonResponse(context)
    return response


# 创建webservice
@csrf_exempt
def webservice_create(request):
    webservice_name = request.POST['webservice_name']
    webservice_desc = request.POST['webservice_desc']
    webservice_html = request.POST['webservice_html']
    parent = request.POST['parent']
    flag = webservice_service.webservice_add(webservice_name, webservice_desc, webservice_html, parent)
    context = dict()
    if flag == "ok":
        context['msg'] = '添加成功'
        context['code'] = '1'
    else:
        context['msg'] = '添加失败'
        context['code'] = '0'
    response = JsonResponse(context)
    return response


# 创建webservice
@csrf_exempt
def webservice_update(request):
    webservice_name = request.POST['webservice_name']
    webservice_desc = request.POST['webservice_desc']
    webservice_html = request.POST['webservice_html']
    is_active = request.POST['is_active']
    id = request.POST['id']
    flag = webservice_service.webservice_update(webservice_name, webservice_desc, webservice_html, is_active, id)
    context = dict()
    if flag == "ok":
        context['msg'] = '更新成功'
        context['code'] = '1'
    else:
        context['msg'] = '更新失败'
        context['code'] = '0'
    response = JsonResponse(context)
    return response
