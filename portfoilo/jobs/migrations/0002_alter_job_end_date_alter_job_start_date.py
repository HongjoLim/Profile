# Generated by Django 4.1.7 on 2023-02-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]