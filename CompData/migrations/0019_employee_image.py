# Generated by Django 2.1.2 on 2018-11-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompData', '0018_auto_20181031_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, upload_to='best_employee'),
        ),
    ]
