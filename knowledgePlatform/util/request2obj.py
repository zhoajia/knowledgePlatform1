from django.forms import model_to_dict
from django.http import JsonResponse

from knowledgePlatform.util.action_enum import ActionEnum
from knowledgePlatform.log_info.models import LogInfoEntity
import datetime


def request2obj(obj, request):
    """
    request转obj
    :param obj:
    :param request:
    :return:
    """
    d = obj.__dict__
    ks = list(d.keys())  # 获取keys列表
    ks.remove("_state")
    # 筛选出定义好的外键
    func_list = [func for func in dir(obj) if func.startswith("pk_")]
    for item in ks:
        if item == 'id' and request.POST.get(item) == '':  # 如果传过来的id为空则不替换
            continue
        setattr(obj, item, request.POST.get(item))
    return obj


def create_update_log(title=None, obj=None, obj_name=None):
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
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        info = ""
        if obj is None:
            info = "修改了'{}'".format(title)
        else:
            info = "修改了'{}'".format(getattr(obj, obj_name))
        login_info = LogInfoEntity()
        login_info.text = info
        login_info.create_date = date
        login_info.save()

    return update_log


def response_body(flag: bool, action_type: str, date: object, total=0):
    """
    返回response
    :param flag: 是否执行成功
    :param action_type: add/update/delete/execute/cancel： 添加/更新/删除/执行/取消
    :param date: 可以为空
    :param total 分页的总数量
    :return:
    """

    context = dict()
    if flag:
        context['msg'] = '{name}成功'.format(name=action_type.value)
        context['code'] = '1'
    else:
        context['msg'] = '{name}失败'.format(name=action_type.value)
        context['code'] = '0'
    if date is None:
        context['data'] = ""
    else:
        context['data'] = date
    context['total'] = total if total is not None else 0
    response = JsonResponse(context)
    return response


def queryset2dict(obj, queryset):
    """
    将queryset 转成 dict
    :param obj: 对象
    :param queryset: 查询的值
    :return:
    """
    l = list()
    d = obj.__dict__
    ks = list(d.keys())  # 获取keys列表
    ks.remove("_state")
    # 筛选出定义好的外键
    func_list = [func for func in dir(obj) if func.startswith("pk_")]
    # 处理将queryset 转dict
    for item in queryset:
        obj_dict = dict()
        for key in ks:
            # 根据属性名利用reflect获取到属性值并加入到dict中
            obj_dict[key] = getattr(item, key, "")
        for f in func_list:
            # 根据预先定义好的方法获取外键对象
            pk_str = getattr(obj, f)()
            obj_dict[pk_str] = model_to_dict(getattr(item, pk_str, ""))  # 此处不再考虑外键对象还存在的外键引用对象以防止内存溢出
        l.append(obj_dict)
    return l


def queryset2defined_dict(queryset, *args):
    """
    将queryset 转成 指定的 dict
    :param queryset:
    :param args:
    :return:
    """
    l = list()
    # 处理将queryset 转dict
    for item in queryset:
        obj_dict = dict()
        for key in args:
            # 根据属性名利用reflect获取到属性值并加入到dict中
            obj_dict[key] = getattr(item, key, "")
        l.append(obj_dict)
    return l
