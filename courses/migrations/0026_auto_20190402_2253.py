# Generated by Django 2.1.1 on 2019-04-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_auto_20190402_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='app_force_update',
        ),
        migrations.AddField(
            model_name='school',
            name='app_support_version',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
