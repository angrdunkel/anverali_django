# Generated by Django 5.0.4 on 2024-05-03 09:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_remove_taskroom_created_at_task_complite_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskroom',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_customer', to=settings.AUTH_USER_MODEL, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='taskroom',
            name='performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_performer', to=settings.AUTH_USER_MODEL, verbose_name='Performer'),
        ),
        migrations.AlterField(
            model_name='taskroom',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_room', to='task.task', verbose_name='Task'),
        ),
    ]
