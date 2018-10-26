# Generated by Django 2.1.2 on 2018-10-26 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompData', '0009_auto_20181026_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='product_name',
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CompData.Product'),
        ),
    ]
