# Generated by Django 3.2.6 on 2021-09-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aniuser', '0002_alter_aniuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aniuser',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码'),
        ),
    ]
