# Generated by Django 5.0 on 2023-12-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_uploadfile_file_id_sharedfiles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharedfiles',
            old_name='files',
            new_name='sharefiles',
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file_id',
            field=models.CharField(default='6e37e3a16ec9', editable=False, max_length=255),
        ),
    ]
