# Generated by Django 2.2.12 on 2020-08-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='image',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='tutorials/'),
        ),
    ]
