# Generated by Django 4.2.3 on 2023-07-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0007_alter_advertisment_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='advertisment',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
