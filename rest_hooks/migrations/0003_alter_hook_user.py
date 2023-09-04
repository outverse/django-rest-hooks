# Generated by Django 4.2.4 on 2023-09-04 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_hooks', '0002_swappable_hook_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
    ]
