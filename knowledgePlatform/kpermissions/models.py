from django.db import models

# Create your models here.
import uuid
from django.db import models
from knowledgePlatform.sub_type.models import SubType


# 权限model
class KpermissionsEntity(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 分类名称
    permissions_name = models.CharField(max_length=20)
    # 所属模块
    sub_type = models.ForeignKey("sub_type.SubType", on_delete=1, default=None)
    # 是否激活 (0 冻结 1 激活)
    is_active = models.IntegerField()
    # 创建日期
    create_date = models.DateTimeField('date published')
    # 最后修改日期
    update_date = models.DateTimeField('date modified')

    def pk_sub_type(self):
        return "sub_type"

    class Meta:
        db_table = "k_permissions"  # 自定义创建的表名
