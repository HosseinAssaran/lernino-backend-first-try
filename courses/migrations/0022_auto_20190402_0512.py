# Generated by Django 2.1.1 on 2019-04-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_course_lessons_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='apkAddress',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='apkForceUpdate',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='apkLastVersion',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]