# Generated by Django 4.0 on 2022-01-05 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_created_at_alter_item_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
