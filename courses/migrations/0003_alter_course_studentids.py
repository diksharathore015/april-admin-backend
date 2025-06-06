# Generated by Django 5.1.7 on 2025-04-08 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allstudents', '0003_alter_student_courses'),
        ('courses', '0002_course_studentids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='studentids',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='allstudents.student'),
        ),
    ]
