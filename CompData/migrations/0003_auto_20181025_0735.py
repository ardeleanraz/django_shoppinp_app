# Generated by Django 2.1.2 on 2018-10-25 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompData', '0002_auto_20181025_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CompData.Employee'),
        ),
    ]
