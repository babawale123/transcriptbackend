# Generated by Django 4.2.4 on 2023-10-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcriptmodel',
            name='level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transcriptmodel',
            name='score',
            field=models.IntegerField(),
        ),
    ]
