# Generated by Django 3.2.6 on 2021-08-25 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0002_remove_tag_tag_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]
