from django.db import models

# Create your models here.
'''
    $ python manage.py migrate   # 创建表结构
    $ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
    $ python manage.py migrate TestModel   # 创建表结构
'''

from django.db import models
import uuid


class UserEntity(models.Model):
    # 主键uuid
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 用户名
    user_name = models.CharField(max_length=20)
    # 密码
    pass_word = models.CharField(max_length=200)
    # 创建日期
    create_date = models.DateField('date published')
    # 最后修改日期
    update_date = models.DateField('最后修改日期', blank=True, null=True)

    class Meta:
        db_table = "user"  # 自定义创建的表名
