# Generated by Django 4.1.7 on 2023-03-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_menagement_app', '0003_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Nowy', 'Nowe zadanie'), ('W toku', 'W trakcie realizacji'), ('Rozwiązany', 'Zadanie rozwiązane')], default='Nowy', max_length=32),
        ),
    ]
