# Generated by Django 2.2.3 on 2019-07-22 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20190719_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentity',
            name='update_date',
            field=models.DateField(blank=True, null=True, verbose_name='最后修改日期'),
        ),
    ]
