# Generated by Django 3.2.6 on 2021-09-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='learningresources',
            options={'ordering': ['order', 'id'], 'verbose_name': '学习资源', 'verbose_name_plural': '学习资源'},
        ),
        migrations.AddField(
            model_name='learningresources',
            name='order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='排序'),
        ),
    ]
