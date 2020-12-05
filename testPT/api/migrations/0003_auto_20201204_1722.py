# Generated by Django 3.1.3 on 2020-12-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201128_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='case_check',
            field=models.CharField(max_length=4500, null=True, verbose_name='用例检查点'),
        ),
        migrations.AlterField(
            model_name='api',
            name='case_status',
            field=models.CharField(choices=[('1', '不加密'), ('2', '加密')], default='1', max_length=4, verbose_name='用例状态'),
        ),
    ]