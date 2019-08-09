from django.db import models

# Create your models here.
import uuid
from django.db import models


class TopType(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 分类名称
    type_name = models.CharField(max_length=20)
    # 是否激活 (0 冻结 1 激活)
    is_active = models.IntegerField()
    # 备注
    desc = models.CharField(max_length=20,blank=True)
    # 创建日期
    create_date = models.DateTimeField('date published')
    # 最后修改日期
    update_date = models.DateTimeField('date modified')

    class Meta:
        db_table = "top_type"  # 自定义创建的表名
