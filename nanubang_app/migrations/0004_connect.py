# Generated by Django 2.0.13 on 2019-11-29 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nanubang_app', '0003_auto_20191127_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buy', to=settings.AUTH_USER_MODEL, verbose_name='구매자')),
                ('Room_seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sell', to=settings.AUTH_USER_MODEL, verbose_name='판매자')),
            ],
        ),
    ]
