# Generated by Django 2.1.2 on 2018-10-28 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CompData', '0012_auto_20181026_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='departament',
        ),
    ]
