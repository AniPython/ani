# Generated by Django 3.2.6 on 2021-08-25 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('tag_type', models.CharField(choices=[('1', 'common'), ('2', 'custom')], max_length=2)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('content', tinymce.models.HTMLField(verbose_name='正文')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('tag', models.ManyToManyField(to='snippet.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '代码片段',
                'verbose_name_plural': '代码片段',
                'ordering': ['-create_time'],
            },
        ),
    ]
