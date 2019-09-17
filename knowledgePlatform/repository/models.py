from django.db import models

# Create your models here.
import uuid
from django.db import models


class RepositoryEntity(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 父类id
    parent_id = models.UUIDField(blank=False,max_length=50)

    # 等级(0-99)
    level = models.IntegerField()

    # 名称
    repository_name = models.CharField(max_length=10)

    # 类型
    repository_type = models.IntegerField()

    # 是否激活 (0 冻结 1 激活)
    is_active = models.IntegerField(default=1)

    # 备注
    desc = models.CharField(max_length=20, blank=True ,null=True)

    # 创建日期
    create_date = models.DateTimeField('date published',)

    # 最后修改日期
    update_date = models.DateTimeField('date modified')

    class Meta:
        db_table = "repository"  # 自定义创建的表名
