# Generated by Django 5.0 on 2023-12-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_file_uploadfile_uploading_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file_id',
            field=models.CharField(default='2be9a7415ee5', editable=False, max_length=255),
        ),
    ]
