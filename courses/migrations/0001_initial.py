# Generated by Django 2.1.1 on 2018-08-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('iconAddr', models.CharField(max_length=256)),
                ('relAddr', models.CharField(max_length=256)),
                ('numInRow', models.IntegerField(null=True)),
            ],
        ),
    ]