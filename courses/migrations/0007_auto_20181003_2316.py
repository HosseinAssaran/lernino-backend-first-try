# Generated by Django 2.1.1 on 2018-10-03 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20180927_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]
