# Generated by Django 3.1.6 on 2021-03-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_order_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='capital',
            field=models.BooleanField(default=False),
        ),
    ]
