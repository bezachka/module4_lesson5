# Generated by Django 4.2.3 on 2023-08-17 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisment', '0008_alter_advertisment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
