import datetime
from knowledgePlatform.kpermissions.models import KpermissionsEntity
from django.core.paginator import Paginator

# 获得所有的权限
from knowledgePlatform.sub_type.models import SubType
from knowledgePlatform.util.request2obj import queryset2dict


def get_all_permission(page_number):
    permission_list = KpermissionsEntity.objects.all().order_by("sub_type")
    total = len(permission_list)
    paginator = Paginator(permission_list, 10)
    permission_list = paginator.page(page_number).object_list
    return permission_list, total


# 创建权限
def permission_create(permission_entity: KpermissionsEntity):
    # 查询名称是否重复
    same_name = KpermissionsEntity.objects.filter(is_active=1, permissions_name=permission_entity.permissions_name)
    if len(same_name):
        return False
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    permission_entity.create_date = date
    permission_entity.update_date = date
    permission_entity.is_active = 1
    permission_entity.save()
    return True


# 查询权限列表（树形加载:element UI 结构）
def load_permission_tree():
    parent_list = list()  # 父节点
    sub_type_list = SubType.objects.all()
    for sub_type_item in sub_type_list:
        parent_dict = dict()  # 父节点元素

        sub_type_id = sub_type_item.id  # 模块id

        parent_dict['id'] = sub_type_id
        parent_dict['label'] = sub_type_item.type_name

        children_list = []  # 权限节点list

        # select permission by sub_type_id
        permission_list = KpermissionsEntity.objects.filter(sub_type_id=sub_type_id)
        for permission_item in permission_list:
            children_dict = dict()
            children_dict['id'] = permission_item.id
            children_dict['label'] = permission_item.permissions_name
            children_list.append(children_dict)

        parent_dict['children'] = children_list
        parent_list.append(parent_dict)

    return parent_list