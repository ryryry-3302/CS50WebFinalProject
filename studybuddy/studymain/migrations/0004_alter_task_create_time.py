# Generated by Django 4.0.4 on 2022-09-17 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studymain', '0003_task_modified_alter_task_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
    ]