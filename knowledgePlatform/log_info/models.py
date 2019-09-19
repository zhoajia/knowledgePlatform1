from django.db import models
import uuid


# Create your models here.
class LogInfoEntity(models.Model):
    # 主键uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    text = models.CharField(max_length=100)

    create_date = models.DateTimeField('date published', )

    class Meta:
        db_table = "log_info"  # 自定义创建的表名