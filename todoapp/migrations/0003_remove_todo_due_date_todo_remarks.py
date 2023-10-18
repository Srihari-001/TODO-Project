# Generated by Django 4.2.5 on 2023-10-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todo_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='due_date',
        ),
        migrations.AddField(
            model_name='todo',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
