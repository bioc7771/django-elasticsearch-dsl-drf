# Generated by Django 3.1.6 on 2021-03-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_merge_20210219_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
