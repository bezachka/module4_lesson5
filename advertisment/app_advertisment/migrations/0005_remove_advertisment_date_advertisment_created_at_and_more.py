# Generated by Django 4.2.3 on 2023-07-29 11:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0004_advertisment_auction_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisment',
            name='date',
        ),
        migrations.AddField(
            model_name='advertisment',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisment',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisment',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
    ]
