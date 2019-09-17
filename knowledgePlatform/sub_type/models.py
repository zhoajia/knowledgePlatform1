from django.db import models

# Create your models here.
import uuid
from knowledgePlatform.top_type.models import TopType
from django.db import models


class SubType(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 一级分类id
    parent = models.ForeignKey("top_type.TopType",on_delete=1)
    # 分类名称
    type_name = models.CharField(max_length=20)
    # 连接地址
    type_url = models.CharField(max_length=50,blank=True)
    # 是否激活 (0 冻结 1 激活)
    is_active = models.IntegerField(default=1)
    # 备注
    desc = models.CharField(max_length=20,blank=True)
    # 创建日期
    create_date = models.DateTimeField('date published')
    # 最后修改日期
    update_date = models.DateTimeField('date modified')

    class Meta:
        db_table = "sub_type"  # 自定义创建的表名
