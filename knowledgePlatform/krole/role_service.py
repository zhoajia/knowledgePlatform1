import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator

from knowledgePlatform.kpermissions.models import KpermissionsEntity
from knowledgePlatform.krole.models import KroleEntity, AuthUser2RoleEntity
from knowledgePlatform.util.queryUtil import find_by_page


def get_role_list(page_number):
    """
    分页查询角色
    :param page_number:
    :return:
    """
    role_list = KroleEntity.objects.all().order_by("create_date")
    return find_by_page(role_list, page_number)


def create_role(role_entity: KroleEntity):
    if len(KroleEntity.objects.filter(is_active=1, role_name=role_entity.role_name)) > 0:
        return False
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    role_entity.create_date = date
    role_entity.update_date = date
    role_entity.is_active = 1
    role_entity.save()
    return True


def get_user_by_role_id(role_id):
    # user2role_list = AuthUser2RoleEntity.objects.filter(role_id=role_id)  # 用户角色关联表
    user_list = User.objects.filter(authuser2roleentity__role__id=role_id)
    return user_list


def get_permissions_by_role_id(role_id):
    permission_list = KpermissionsEntity.objects.filter(krole2kpermissionsentity__role__id=role_id)
    return permission_list
