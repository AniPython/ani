# Generated by Django 3.2.6 on 2021-08-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20210825_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.CharField(max_length=32, null=True, verbose_name='评论对象ID'),
        ),
    ]