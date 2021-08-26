# Generated by Django 3.2.6 on 2021-08-25 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='object_id',
            field=models.CharField(max_length=64, null=True, verbose_name='评论对象ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='评论内容'),
        ),
    ]
