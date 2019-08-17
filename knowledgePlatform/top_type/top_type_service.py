from knowledgePlatform import top_type

# 创建类型
from knowledgePlatform.top_type.models import TopType
import datetime


def creat_type(name):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    t = TopType()
    t.type_name = name
    t.is_active = 1
    t.create_date = date
    t.update_date = date
    t.save()
    return "ok";


def update_top_type(_top_type: TopType):
    old_top_type = TopType.objects.get(id=_top_type.id)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    old_top_type.type_name = _top_type.type_name
    old_top_type.update_date = date
    old_top_type.is_active = _top_type.is_active
    old_top_type.save()
    return "ok"
