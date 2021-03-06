# Generated by Django 2.2.12 on 2020-09-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_tutorial_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='lang',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='docs/tutorials/'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/tutorials/'),
        ),
    ]
