# Generated by Django 3.1.3 on 2020-11-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201111_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='createtime',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
    ]
