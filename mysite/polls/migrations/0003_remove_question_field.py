# Generated by Django 3.1.2 on 2020-10-27 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='field',
        ),
    ]
