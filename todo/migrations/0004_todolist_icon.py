# Generated by Django 5.0.6 on 2024-06-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_items_task_rename_lists_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='icon',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
