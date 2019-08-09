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