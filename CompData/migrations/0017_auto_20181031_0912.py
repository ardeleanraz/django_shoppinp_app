# Generated by Django 2.1.2 on 2018-10-31 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CompData', '0016_auto_20181029_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departament',
            old_name='manager',
            new_name='employee',
        ),
    ]
