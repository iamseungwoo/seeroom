# Generated by Django 3.2 on 2022-07-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20220714_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewtest',
            name='recommend',
            field=models.IntegerField(default=0, null=True),
        ),
    ]