# Generated by Django 4.1.7 on 2023-04-08 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_group_g_course_alter_group_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='number',
            new_name='name',
        ),
    ]