# Generated by Django 3.0.7 on 2021-04-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210421_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='meet_link',
            field=models.URLField(default='', help_text='Add the drive link to your resume.'),
        ),
    ]
