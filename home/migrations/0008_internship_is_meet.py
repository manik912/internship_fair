# Generated by Django 3.0.7 on 2021-04-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_internship_meet_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='is_meet',
            field=models.BooleanField(default=True),
        ),
    ]
