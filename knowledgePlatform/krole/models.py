from django.db import models

# Create your models here.
import uuid
from django.db import models


# 角色model
class KroleEntity(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 分类名称
    role_name = models.CharField(max_length=20)
    # 是否激活 (0 冻结 1 激活)
    is_active = models.IntegerField()
    # 备注
    desc = models.CharField(max_length=20, blank=True)
    # 创建日期
    create_date = models.DateTimeField('date published')
    # 最后修改日期
    update_date = models.DateTimeField('date modified')

    class Meta:
        db_table = "k_role"  # 自定义创建的表名


# 角色权限对应关系（一对多）
class Krole2KpermissionsEntity(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 分类id
    role = models.ForeignKey("KroleEntity", on_delete=1)
    # 权限id
    permission = models.ForeignKey("kpermissions.KpermissionsEntity", on_delete=1)

    # 创建日期
    create_date = models.DateTimeField('date published')
    # 最后修改日期
    update_date = models.DateTimeField('date modified')

    class Meta:
        db_table = "k_role2permissions"  # 自定义创建的表名


# 用户角色对应关系
class AuthUser2RoleEntity(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 分类id
    role = models.ForeignKey("KroleEntity", on_delete=1)
    # 用户id
    user = models.ForeignKey("auth.User", on_delete=1)
    # 创建日期
    create_date = models.DateTimeField('date published')
    # 最后修改日期
    update_date = models.DateTimeField('date modified')

    class Meta:
        db_table = "k_authUser2role"  # 自定义创建的表名
