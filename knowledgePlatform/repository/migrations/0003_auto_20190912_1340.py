# Generated by Django 2.2.3 on 2019-09-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20190905_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositoryentity',
            name='parent_id',
            field=models.UUIDField(),
        ),
    ]
