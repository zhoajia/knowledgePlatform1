import json
from django.forms import model_to_dict
from django.shortcuts import render
from django.core import serializers

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from knowledgePlatform.log_info.models import LogInfoEntity
from django.core.paginator import Paginator
from knowledgePlatform.util.action_enum import ActionEnum
from knowledgePlatform.util.request2obj import response_body


@csrf_exempt
def get_top_log(request):
    log_list = LogInfoEntity.objects.all()
    paginator = Paginator(log_list, 10)
    log_list = paginator.page(1).object_list
    res = response_body(True, ActionEnum.EXECUTE, json.loads(serializers.serialize("json",log_list)))
    return res
