# Generated by Django 2.1.1 on 2018-12-14 09:10

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20181214_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=courses.models.parts_image),
        ),
    ]