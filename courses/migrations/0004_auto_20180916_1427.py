# Generated by Django 2.1.1 on 2018-09-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180916_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='text',
            field=models.TextField(null=True),
        ),
    ]