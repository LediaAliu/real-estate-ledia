# Generated by Django 4.2.11 on 2024-03-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_property_sqm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='sqm',
            field=models.PositiveIntegerField(help_text='in SQM', verbose_name='Area'),
        ),
    ]