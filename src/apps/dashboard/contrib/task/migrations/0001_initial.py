# Generated by Django 5.0.4 on 2024-05-02 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title for task', max_length=255, verbose_name='Title')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='TaskRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='task_customer', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('performer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='task_performer', to=settings.AUTH_USER_MODEL, verbose_name='Performer')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='task_room', to='task.task', verbose_name='Task')),
            ],
        ),
    ]
