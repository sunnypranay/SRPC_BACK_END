# Generated by Django 4.1.7 on 2023-04-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
