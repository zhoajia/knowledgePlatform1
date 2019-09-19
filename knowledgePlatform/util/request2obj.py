from django.http import JsonResponse

from knowledgePlatform.util.action_enum import ActionEnum


def request2obj(obj, request):
    d = obj.__dict__
    ks = list(d.keys())  # 获取keys列表
    ks.remove("_state")
    for item in ks:
        if item == 'id' and request.POST.get(item) == '':  # 如果传过来的id为空则不替换
            continue
        setattr(obj, item, request.POST.get(item))
    return obj


def create_update_log(title = None,obj = None, obj_name = None):
    """
    根据传过来的的对象记录对象的修改记录
    这是一个AOP方法
    :param obj: 待修改的对象
    :param obj_name: 取对应对象的属性
    :param title: 修改内容
    :return: null
    """

    def update_log():
        # 执行对应的sql
        info = ""
        if obj is None:
            info = "修改了'{}'".format(title)
        else:
            info = "修改了'{}'".format(getattr(obj, obj_name))

    return update_log


def response_body(flag: bool, action_type: str, date: object):
    """
    返回response
    :param flag: 是否执行成功
    :param action_type: add/update/delete/execute/cancel： 添加/更新/删除/执行/取消
    :param date:
    :return:
    """

    context = dict()
    if flag:
        context['msg'] = '{name}成功'.format(name=action_type)
        context['code'] = '1'
    else:
        context['msg'] = '{name}失败'.format(name=action_type)
        context['code'] = '0'
    if date is None:
        context['data'] = ""
    else:
        context['data'] = date
    response = JsonResponse(context)
    return response
