# Generated by Django 4.2.3 on 2023-07-05 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_collection', '0004_rename_place_publishplace_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publishplace',
            old_name='name',
            new_name='pname',
        ),
        migrations.RenameField(
            model_name='subjectplace',
            old_name='name',
            new_name='pname',
        ),
    ]
