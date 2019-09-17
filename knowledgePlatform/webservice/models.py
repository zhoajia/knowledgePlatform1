import uuid
from django.db import models
from knowledgePlatform.repository.models import RepositoryEntity


# webservice
class WebServiceEntity(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 二级分类id
    parent = models.ForeignKey("repository.RepositoryEntity", on_delete=1)
    # 名称
    webservice_name = models.CharField(max_length=50)
    # 接口释义
    webservice_desc = models.TextField(blank=True)
    # 接口html(富文本编辑器)
    webservice_html = models.TextField(blank=True)
    # 返回值释义(富文本编辑器)
    webservice_res_desc = models.TextField(blank=True)
    # 备注
    desc = models.CharField(max_length=20, blank=True)
    # 创建日期
    create_date = models.DateTimeField('date published')
    # 最后修改日期
    update_date = models.DateTimeField('date modified')
    # 是否激活 (0 冻结 1 激活)
    is_active = models.IntegerField(default=1)

    class Meta:
        db_table = "web_service"  # 自定义创建的表名


# webservice 参数
class WebServiceParam(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # webserviceId
    webservice = models.ForeignKey("webservice.WebServiceEntity", on_delete=1)
    # 类型 1.参数 2.返回参数
    type = models.IntegerField()
    # paramName
    param_name = models.CharField(max_length=50)
    # paramValue
    param_value = models.CharField(max_length=50)
    # 创建日期
    create_date = models.DateTimeField('date published')
    # 最后修改日期
    update_date = models.DateTimeField('date modified')
    # 是否激活 (0 冻结 1 激活)
    is_active = models.IntegerField(default=1)

    class Meta:
        db_table = "web_service_param"  # 自定义创建的表名
