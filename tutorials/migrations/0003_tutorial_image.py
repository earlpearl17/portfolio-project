# Generated by Django 2.2.12 on 2020-08-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20200823_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tutorials/'),
        ),
    ]
