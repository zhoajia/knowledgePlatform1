from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from knowledgePlatform.top_type import top_type_service
from django.views.decorators.csrf import csrf_exempt,csrf_protect


# Create your views here.
# @csrf_exempt 关闭csrf验证
@csrf_exempt
def create_top_type(request):
    flag = top_type_service.creat_type(request.POST['type_name'])
    if flag == 'ok':
        context = dict()
        context['msg'] = '添加成功'
        context['code'] = '1'
        response = JsonResponse(context)
        return response