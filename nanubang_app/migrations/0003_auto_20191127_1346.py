# Generated by Django 2.0.13 on 2019-11-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanubang_app', '0002_auto_20191127_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_infos',
            name='photo2',
            field=models.ImageField(blank=True, default='./default/img_icon_temp.png', null=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='room_infos',
            name='photo3',
            field=models.ImageField(blank=True, default='./default/img_icon_temp.png', null=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='room_infos',
            name='photo4',
            field=models.ImageField(blank=True, default='./default/img_icon_temp.png', null=True, upload_to='%Y/%m/%d'),
        ),
    ]
