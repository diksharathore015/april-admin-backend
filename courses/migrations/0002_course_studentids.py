# Generated by Django 5.1.7 on 2025-04-08 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allstudents', '0002_alter_student_image'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='studentids',
            field=models.ManyToManyField(related_name='students', to='allstudents.student'),
        ),
    ]
