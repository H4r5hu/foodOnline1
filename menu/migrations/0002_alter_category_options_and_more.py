# Generated by Django 5.0.1 on 2024-03-05 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='fooditem',
            old_name='Category',
            new_name='category',
        ),
    ]
